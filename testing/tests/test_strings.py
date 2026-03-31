import pytest


def test_attempt_to_substitute_letter_raises_exception() -> None:
    a_string = "example"
    with pytest.raises(TypeError):
        a_string[0] = "a"
