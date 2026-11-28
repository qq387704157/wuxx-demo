# 贡献指南

感谢你愿意改进 wuxx-demo！

## 提交流程

1. Fork 本仓库并克隆到本地
2. 创建特性分支：`git checkout -b feature/你的主题`
3. 修改代码并确保测试通过：`python -m unittest discover -s tests -v`
4. 提交：`git commit -m "feat: 简短描述"`
5. 推送分支并创建 Pull Request

## 提交信息规范

- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `chore:` 构建/工程化
- `test:` 测试相关

## 代码规范

- 保持函数职责单一
- 为新增逻辑补充单元测试
- 提交前本地跑一遍测试
