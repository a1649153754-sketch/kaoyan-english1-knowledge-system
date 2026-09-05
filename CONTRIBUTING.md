# 贡献指南

感谢补充或纠错。提交前请遵守：

1. 不上传未经授权的真题全文、文章全文、教材或付费课程内容。
2. 新节点必须说明触发信号、方法、边界和掌握证据。
3. 旧编号尽量不改；新增编号按现有序列追加。
4. 解析应区分原文证据、合理推断和个人经验。
5. 运行：

```bash
python scripts/validate_project.py
python scripts/build_bundle.py
zensical build --clean --strict
```

Pull Request 中请说明修改模块、原因、验证方式和是否影响编号。
