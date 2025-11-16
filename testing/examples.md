cd testing

# Run tests
python3.14 -m unittest

# Run tests and show tests names
python3.14 -m unittest -v

# Run tests in specific TestCase class
python3.14 -m unittest module_name.TestCaseClassName
e.g.
python3.14 -m unittest test_example_unittest.ExampleAssertions

# Run specifc test
python3.14 -m unittest module_name.TestCaseClassName.method_name
e.g.
python3.14 -m unittest test_example_unittest.ExampleAssertions.test_
