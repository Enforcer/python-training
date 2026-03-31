import pytest


def test_basic() -> None:
    """Simplest test. A function, its name MUST start `test`."""

    # just assert keyword, followed by boolean expression
    assert True


class TestClass:
    """A class can be used to group tests."""

    def test_method(self) -> None:
        """Test method, its name also MUST start with `test`."""
        pass


@pytest.fixture()
def empty_list() -> list:
    """A function decorated with `pytest.fixture` becomes reusable across tests.

    To use it in the test, just declare a test function with the same name as fixture.

    By default, fixture function is called for each test.
    Thus, every test receives a fresh, empty list.

    To reuse same fixture across tests, use `scope`
    argument to `pytest.fixture` decorator.
    """
    return []


def test_empty_list_has_size_0(empty_list: list) -> None:
    assert len(empty_list) == 0


def test_index_raises_index_error_for_absent_element(empty_list: list) -> None:
    with pytest.raises(ValueError):
        empty_list.index(0)


def is_underage(age: int) -> bool:
    """Function to be tested."""
    return age < 18


@pytest.mark.parametrize("age", [1, 2, 3])
def test_underage_detection(age: int) -> None:
    """Parametrized test.

    It will be executed 3 times, once for each value in `age` list.
    """
    result = is_underage(age)

    assert result is True
