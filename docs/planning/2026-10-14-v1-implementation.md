# Liyuk Skills v0.1 Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans for inline implementation. User explicitly requested completion in this session.

**Goal:** 分析 Matt 设计，发布八项技能的可安装第一版与公开 GitHub 仓库。
**Architecture:** Ask Liyuk 导航，独立技能执行，包内参考保存方法；JSON 目录用于一致性检查。
**Tech Stack:** Markdown、JSON、YAML、Python 3.10+、PyYAML 6.x、GitHub Actions。
**Spec:** ../design/2026-10-14-v1-design.md

## Global Constraints

- 首版八项技能，Ask 和 distill-experience 显式调用，其余默认发现。
- 成熟包自包含，外部来源仅用于追溯。
- 保留五项工程技能许可与39个历史案例；新案例不是已完成评测。
- 发布公开 Liyuk/skills，不发布私人经历或未授权来源全文。

## Review Focus

- 文件引用存在却位于包外：拒绝，干净复制应仍能使用。
- 调用元数据与 catalog 不一致：拒绝，避免路由误导。
- 可读 JSON 缺字段或有重复项：产生明确错误。
- 未安装其他技能：Ask 应给出下一步，不假装完成。
- 蒸馏材料不足或作者意见未确认：保留候选状态，不冒充作者。

## Task 1: Sources and skills

- [x] 复制五项技能与历史案例，修复引用，登记文件指纹。
- [x] 编写 Ask Liyuk、experience-review、distill-experience 及各自参考、案例、元数据。
- [x] 编写 README、AGENTS、LICENSE、插件配置与变更记录。

## Task 2: Validation

**Interface:** scripts/validate_repo.py: validate(root: Path) -> list[str]，命令行退出码0表示通过，1表示错误。

- [x] tests/test_validate_repo.py 使用临时技能包，覆盖有效目录、包外与缺失引用、错名、元数据冲突、重复案例、发布清单漂移。
- [x] python -m unittest discover -s tests -v；确认缺少校验器导致失败。
- [x] 实现校验器并执行测试与整仓校验。
- [x] 添加 CI，验证单项复制与既有脚本样例。

## Task 3: Review and publish

- [x] 独立评审新技能与目录，记录行为冒烟范围和结果。
- [x] 修复实际发现，再执行全部检查。
- [ ] 初始化并提交 Git；创建公开远端并推送。
- [ ] 核对远端可见性、commit 与 CI，交付链接。
