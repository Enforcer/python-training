import unittest


class ExampleTest(unittest.TestCase):
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_1(self) -> None:
        print("test_1")

    def test_2(self) -> None:
        print("test_2")


class ExampleAssertions(unittest.TestCase):
    def test_(self) -> None:
        self.assertTrue(True)
        self.assertEqual(False, False)
        self.assertIsInstance(5, int)
        self.assertDictEqual({"key": 1}, {"key": 1.0})
        self.assertIsNone(None)
        with self.assertRaises(ValueError):
            int("no, can't do that")


if __name__ == "__main__":
    unittest.main()
