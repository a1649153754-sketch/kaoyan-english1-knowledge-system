# 项目维护指南

## 17.1 日常更新位置

- 正文节点：`docs/01-...md` 至 `docs/08-...md`
- 检查项：`docs/10-checklists.md`
- 规则卡：`docs/11-rule-cards.md`
- 母题：`docs/13-problem-archetypes.md`
- 边界卡：`docs/14-counterexamples.md`
- 个人疑问：`docs/15-personal-links.md`
- 个人数据：`data/`
- 官方范围与年度核对：`docs/18-official-scope.md`

## 17.2 编号原则

1. 旧编号一旦进入真题/错题记录，尽量不重排。
2. 新节点在同一前缀下追加；弃用节点保留并标记 deprecated。
3. 规则卡使用 `K-节点-序号`，母题使用 `Q-模块序号`。
4. 只在有真实题目或清晰边界时新增卡片，避免为追求数量堆名词。

## 17.3 发布流程

```bash
python scripts/validate_project.py
python scripts/build_bundle.py
zensical build --clean
```

然后更新 `VERSION`、`CHANGELOG.md`，提交分支并创建 Pull Request。

## 17.4 版权边界

- 可记录真题年份、题号、考点、答案证据摘要与自己的解析。
- 不上传未经授权的整套试卷扫描件、文章全文、付费课程讲义或大段教材。
- 原创例句尽量简短，避免复刻真题句子。

## 17.5 v1.1 优先路线

1. 挂接 2000—2026 年个人已做真题的年份、题号、正确率和用时。
2. 为翻译和写作建立个人二稿库。
3. 将 J-01—J-12 的历史问题补齐证据与复测结果。
4. 生成个人薄弱节点热力图，而不是继续无边界扩充。
