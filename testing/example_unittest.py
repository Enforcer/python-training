import unittest


class ExampleTest(unittest.TestCase):
    def test_adding(self) -> None:
        result = 1 + 2
        expected = 3

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
