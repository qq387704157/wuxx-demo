"""一个极简的问候模块，用作工程化示例。"""


def greet(name: str = "world") -> str:
    """返回一句友好的问候语。

    Args:
        name: 要问候的名字。

    Returns:
        形如 ``Hello, <name>!`` 的字符串。

    Raises:
        TypeError: 当 name 不是字符串时。
        ValueError: 当 name 为空或全为空白时。
    """
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
