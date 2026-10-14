#!/usr/bin/env python3
"""Validate published skill packages and their repository metadata, without mutation."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f'duplicate YAML key: {key}')
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []

    def error(message):
        errors.append(message)

    def read_json(path):
        try:
            return json.loads(path.read_text())
        except (OSError, ValueError) as exc:
            error(f'{path.relative_to(root)}: invalid or missing JSON: {exc}')
            return None

    def read_yaml(path, frontmatter=False):
        try:
            text = path.read_text()
            if frontmatter:
                match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
                if not match:
                    raise ValueError('missing YAML frontmatter')
                text = match.group(1)
            value = yaml.load(text, Loader=UniqueLoader)
            if not isinstance(value, dict):
                raise ValueError('YAML must be a mapping')
            return value
        except (OSError, ValueError, yaml.YAMLError, TypeError) as exc:
            error(f'{path.relative_to(root)}: invalid YAML: {exc}')
            return {}

    catalog = read_json(root / 'catalog/skills.json')
    sources = read_json(root / 'catalog/sources.json')
    if not isinstance(catalog, dict) or not isinstance(catalog.get('skills'), list):
        error('catalog skills must be a list')
        return errors
    source_ids = set()
    if not isinstance(sources, dict) or not isinstance(sources.get('sources'), list):
        error('catalog sources must be a list')
    else:
        for source in sources['sources']:
            if not isinstance(source, dict) or not isinstance(source.get('id'), str):
                error('invalid source record')
                continue
            if source['id'] in source_ids:
                error('duplicate source ID: ' + source['id'])
            source_ids.add(source['id'])
            if 'commit' in source and not re.fullmatch(r'[0-9a-f]{40}', str(source['commit'])):
                error('invalid source commit: ' + source['id'])
            records = source.get('files', [])
            if not isinstance(records, list):
                error('invalid source files list: ' + source['id'])
                records = []
            for record in records:
                if not isinstance(record, dict) or not re.fullmatch(r'[0-9a-f]{64}', str(record.get('sha256', ''))):
                    error('invalid source fingerprint: ' + source['id'])

    entries = catalog['skills']
    names, paths = set(), set()
    try:
        readme = (root / 'README.md').read_text()
    except OSError:
        readme = ''
        error('missing README')
    for entry in entries:
        if not isinstance(entry, dict):
            error('invalid skill catalog entry')
            continue
        name, path = entry.get('name'), entry.get('path')
        if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            error('invalid skill name')
            continue
        if name in names:
            error('duplicate skill name: ' + name)
        names.add(name)
        if path != 'skills/' + name:
            error(f'{name}: catalog path must match name')
            continue
        paths.add(path)
        package = root / path
        if not package.is_dir() or not package.resolve().is_relative_to(root / 'skills'):
            error(f'{name}: missing or outside skill package')
            continue
        meta = read_yaml(package / 'SKILL.md', frontmatter=True)
        if meta.get('name') != name:
            error(f'{name}: frontmatter name does not match directory')
        description = meta.get('description')
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            error(f'{name}: invalid description')
        if meta.get('license') != 'MIT' or not (package / 'LICENSE').is_file():
            error(f'{name}: missing MIT license declaration or file')
        invocation = entry.get('invocation')
        ui = read_yaml(package / 'agents/openai.yaml')
        policy = ui.get('policy', {})
        if not isinstance(policy, dict):
            error(f'{name}: invalid invocation policy')
            policy = {}
        explicit = invocation == 'explicit'
        if invocation not in ['explicit', 'automatic'] or meta.get('disable-model-invocation', False) is not explicit or policy.get('allow_implicit_invocation', True) is not (not explicit):
            error(f'{name}: invocation mode conflicts across catalog and client policies')
        interface = ui.get('interface', {})
        if not isinstance(interface, dict) or any(not isinstance(interface.get(k), str) or not interface[k].strip() for k in ['display_name', 'short_description']):
            error(f'{name}: missing client interface metadata')
        refs = entry.get('sources')
        if not isinstance(refs, list) or not refs or any(not isinstance(s, str) or s not in source_ids for s in refs):
            error(f'{name}: missing or unknown source ID')
        if f']({path}/SKILL.md)' not in readme:
            error(f'{name}: missing README link')

        for file in package.rglob('*'):
            if file.is_symlink():
                error(f'{name}: symlink file outside supported self-contained package: {file.name}')
        for md in package.rglob('*.md'):
            for target in re.findall(r'\[[^\]]*\]\(([^\n]+?)\)', md.read_text()):
                target = target.strip().split(' "', 1)[0].strip('<>')
                url = urlsplit(target)
                if url.scheme or target.startswith('#'):
                    continue
                destination = (md.parent / unquote(url.path)).resolve()
                if not destination.is_relative_to(package.resolve()):
                    error(f'{name}: local reference outside package: {target}')
                elif not destination.exists():
                    error(f'{name}: missing local reference: {target}')

        cases = read_json(package / 'evals/evals.json')
        if not isinstance(cases, list) or not cases:
            error(f'{name}: eval cases must be a non-empty list')
            continue
        ids = set()
        for case in cases:
            if not isinstance(case, dict) or any(not isinstance(case.get(k), str) or not case[k].strip() for k in ['id', 'prompt', 'expected_output']):
                error(f'{name}: eval case missing required string fields')
                continue
            if case['id'] in ids:
                error(f'{name}: duplicate eval ID: ' + case['id'])
            ids.add(case['id'])
            files = case.get('files')
            if not isinstance(files, list) or any(not isinstance(f, str) for f in files):
                error(f'{name}: invalid eval files list')
            else:
                for f in files:
                    destination = (package / f).resolve()
                    if not destination.is_relative_to(package.resolve()) or not destination.is_file():
                        error(f'{name}: missing or outside eval fixture: {f}')

    actual = {str(p.parent.relative_to(root)) for p in (root / 'skills').glob('*/SKILL.md')}
    if actual != paths:
        error('skill catalog does not match installable directories')
    plugin = read_json(root / '.claude-plugin/plugin.json')
    marketplace = read_json(root / '.claude-plugin/marketplace.json')
    if not isinstance(plugin, dict) or not isinstance(plugin.get('skills'), list) or any(not isinstance(p, str) for p in plugin.get('skills', [])):
        error('invalid plugin skills list')
    else:
        if set(plugin['skills']) != {'./' + p for p in paths} or len(plugin['skills']) != len(paths):
            error('plugin skills do not match catalog')
        if plugin.get('version') != catalog.get('version') or not re.fullmatch(r'\d+\.\d+\.\d+', str(catalog.get('version', ''))):
            error('plugin version does not match catalog')
    if not isinstance(marketplace, dict) or not isinstance(marketplace.get('plugins'), list) or not isinstance(plugin, dict):
        error('invalid marketplace')
    elif len(marketplace['plugins']) != 1 or not isinstance(marketplace['plugins'][0], dict) or marketplace['plugins'][0].get('name') != plugin.get('name') or marketplace['plugins'][0].get('source') != './':
        error('marketplace does not reference repository plugin')

    router = root / 'skills/ask-liyuk/references/method-map.md'
    if 'ask-liyuk' in names:
        if not router.is_file():
            error('missing router method map')
        else:
            routed = set(re.findall(r'\|\s*([a-z]+(?:-[a-z]+)+)\s*\|', router.read_text()))
            if routed != names - {'ask-liyuk'}:
                error('router method map does not match catalog')
    flows = root / 'skills/ask-liyuk/references/task-flows.md'
    if flows.is_file():
        mentioned = set(re.findall(r'(?<![A-Za-z0-9_-])([a-z]+(?:-[a-z]+)+)(?![A-Za-z0-9_-])', flows.read_text()))
        for unknown in sorted(mentioned - names):
            error('task-flows mentions unknown skill: ' + unknown)
    contracts = list((root / 'skills').glob('*/references/decision-and-review-contract.md'))
    if len({p.read_bytes() for p in contracts}) > 1:
        error('shared decision contract copies have drifted')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print('ERROR:', error)
        return 1
    print('Validated skill packages, references, sources, invocation policies, eval inventory and plugin manifests.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
