"""
Given function is tested and we noticed that the last test is failing if we run it with the rest of the tests.

```bash
python3.14 -m unittest tests.tests_tasks.test_task_3.FunctionTestCase
```

However, if we run the test alone:

```
python3.14 -m unittest tests.tests_tasks.test_task_3.FunctionTestCase.test_appends_4_if_2_and_no_list_given
```

it passes. It looks like an issue with test isolation and one of the other tests affecting results.

Find and fix the bug. Add more tests if it makes sense.

"""
import unittest


def append_squared(number: int, a_list: list[int] = []) -> list[int]:
    squared = number**2
    a_list.append(squared)
    return a_list


class FunctionTestCase(unittest.TestCase):
    def test_appends_1_if_1_and_empty_list_given(self) -> None:
        a_list = []

        result = append_squared(1, a_list)

        self.assertEqual(result, [1])

    def test_appends_1_if_1_and_no_list_given(self) -> None:
        result = append_squared(1)

        self.assertEqual(result, [1])

    def test_appends_4_if_2_and_not_empty_list_given(self) -> None:
        a_list = [1]

        result = append_squared(2, a_list)

        self.assertEqual(result, [1, 4])

    def test_appends_4_if_2_and_no_list_given(self) -> None:
        result = append_squared(2)

        self.assertEqual(result, [4])
