import unittest


class TestStringsImmutability(unittest.TestCase):
    def test_attempt_to_substitute_letter_raises_exception(self) -> None:
        a_string = "example"

        with self.assertRaises(TypeError):
            a_string[0] = "a"
