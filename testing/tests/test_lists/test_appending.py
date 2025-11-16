import unittest


class TestAppending(unittest.TestCase):
    def test_appending_one_el_makes_len_1(self) -> None:
        a_list = []

        a_list.append("example")

        self.assertEqual(len(a_list), 1)


class TestAppendingWithSetUpAndTearDown(unittest.TestCase):
    def setUp(self) -> None:
        self.a_list = []

    def tearDown(self) -> None:
        self.a_list.clear()

    def test_appending_one_el_makes_len_1(self) -> None:
        self.a_list.append("example")

        self.assertEqual(len(self.a_list), 1)
