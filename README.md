# wuxx-demo

一个用于演示标准工程化流程的 Python 示例仓库：可运行的示例代码、单元测试、CI 检查与规范的协作流程。

## 特性

- 零第三方依赖的示例模块 `greeter`
- 基于 `unittest` 的单元测试
- GitHub Actions CI：push 与 PR 自动跑测试
- MIT 许可证、贡献指南、忽略规则齐备

## 快速开始

### 环境要求

- Python 3.9+

### 运行

```bash
python -m src.greeter
```

或作为模块引用：

```python
from src.greeter import greet

print(greet("义乌"))
# Hello, 义乌!
```

### 运行测试

```bash
python -m unittest discover -s tests -v
```

## 目录结构

```text
wuxx-demo/
├── .github/workflows/ci.yml   # CI 配置
├── src/
│   ├── __init__.py
│   └── greeter.py             # 示例模块
├── tests/
│   └── test_greeter.py        # 单元测试
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## 贡献

欢迎提 Issue 与 Pull Request，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

[MIT](LICENSE) © 2026 Wu Xiaoxiang
