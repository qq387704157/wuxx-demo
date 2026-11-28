"""greeter 模块的单元测试。"""

import unittest

from src.greeter import greet


class TestGreet(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_custom_name(self):
        self.assertEqual(greet("义乌"), "Hello, 义乌!")

    def test_strips_whitespace(self):
        self.assertEqual(greet("  小明  "), "Hello, 小明!")

    def test_rejects_empty(self):
        with self.assertRaises(ValueError):
            greet("   ")

    def test_rejects_non_string(self):
        with self.assertRaises(TypeError):
            greet(123)


if __name__ == "__main__":
    unittest.main()
