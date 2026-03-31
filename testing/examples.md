cd testing

# Run tests
uv run pytest

# Run tests and show tests names
uv run pytest -v

# Run tests in specific module
uv run pytest tests/path/to/test_module.py
e.g.
uv run pytest tests/test_lists/test_appending.py

# Run specific test
uv run pytest tests/path/to/test_module.py::test_name_of_the_test
e.g.
uv run pytest tests/test_lists/test_appending.py::TestAppending::test_appending_one_el_makes_len_1
