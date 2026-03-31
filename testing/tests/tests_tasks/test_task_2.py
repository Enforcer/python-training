"""
A function `append_squared` (defined below) has some tests.

We noticed that the last test is failing if we run it with the rest of the tests.

```bash
uv run pytest tests/tests_tasks/test_task_2.py
```

However, if we run the failing test alone:

```bash
uv run pytest tests/tests_tasks/test_task_2.py::test_appends_4_if_2_and_no_list_given
```

it passes. It looks like an issue with test isolation and one of the other tests affecting results.

The actual task:
- run the test suite
- run the failing test alone
- find and fix the bug. Add more tests if it makes sense.

"""


def append_squared(number: int, a_list: list[int] = []) -> list[int]:
    squared = number**2
    a_list.append(squared)
    return a_list


def test_appends_1_if_1_and_empty_list_given() -> None:
    a_list = []

    result = append_squared(1, a_list)

    assert result == [1]


def test_appends_1_if_1_and_no_list_given() -> None:
    result = append_squared(1)

    assert result == [1]


def test_appends_4_if_2_and_not_empty_list_given() -> None:
    a_list = [1]

    result = append_squared(2, a_list)

    assert result == [1, 4]


def test_appends_4_if_2_and_no_list_given() -> None:
    result = append_squared(2)

    assert result == [4]
