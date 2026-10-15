# 贡献方法与纠错

最有帮助的贡献是一个能复现的使用问题：使用哪个技能、输入了什么公开或合成材料、实际回答的哪一步缺少依据、为什么会影响决定，以及期待满足的判断标准。去掉姓名、公司内部信息、凭证与私人对话；不要为了复现上传整份内部材料。

## 修改已有方法

先确认是方法判断、使用边界、来源归属还是入口问题。方法变更补充正常、缺失信息或冲突信息的案例；expected_output写判断标准，实际运行记录另写，不将预期当成已通过。作者的公开来源、本人明确确认与AI候选适配分别标记；一个场景的确认不自动覆盖全部泛化。

引用外部资料时给出作者、可追溯链接和实际阅读范围；不复制整本书、课程或未授权原文。提交的内容应具有可发布的权利；原创贡献按本仓库MIT许可提供，迁入文件保留原许可及来源。

## 修改目录与文档

每项skills/<name>可独立复制，包内本地引用保持自包含，并保留LICENSE。名称、路径、调用策略、使用示例及状态维护在catalog/skills.json，之后运行：

```sh
.venv/bin/python scripts/sync_catalog.py --write
```

README目录、使用说明、客户端元数据和插件清单由脚本同步。Ask Liyuk的任务路径仍需人工维护，其中技能引用用行内代码标记，以便校验目录是否存在。

## 提交与检查

按README配置虚拟环境后，在仓库根目录执行：

```sh
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/validate_repo.py
.venv/bin/python scripts/sync_catalog.py --check
```

修改通过工作分支提交PR，说明问题、修改后的行为、实际检查和未验证范围。PR合并由维护者决定。工作约定见 [PR同步流程](docs/workflows/pr-sync.md)，方法与来源状态见 [目录](catalog/skills.json)。
