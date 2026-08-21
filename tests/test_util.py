import unittest

from src.util import add


class TestUtil(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)


if __name__ == "__main__":
    unittest.main()