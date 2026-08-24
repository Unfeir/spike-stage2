import unittest

from src.util import add, slugify, titlecase


class TestUtil(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(1, 2), 3)

    def test_slugify_lowercases(self) -> None:
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_slugify_collapses_non_alphanumeric_runs(self) -> None:
        self.assertEqual(slugify("Hello   World!!!"), "hello-world")

    def test_slugify_strips_leading_and_trailing_dashes(self) -> None:
        self.assertEqual(slugify("--Hello World--"), "hello-world")

    def test_slugify_treats_underscores_as_separators(self) -> None:
        self.assertEqual(slugify("a_b"), "a-b")

    def test_slugify_empty_string(self) -> None:
        self.assertEqual(slugify(""), "")

    def test_titlecase_capitalizes_each_word(self) -> None:
        self.assertEqual(titlecase("hello world"), "Hello World")

    def test_titlecase_lowercases_rest_of_word(self) -> None:
        self.assertEqual(titlecase("hELLO wORLD"), "Hello World")

    def test_titlecase_empty_string(self) -> None:
        self.assertEqual(titlecase(""), "")


if __name__ == "__main__":
    unittest.main()