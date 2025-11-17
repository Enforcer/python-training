# Try converting items on the list one, in a loop at a time to integers (int()).
# When it fails, catch the appropriate exception and use -1.
# Instead of swallowing the exception, add it to another list and build exception group.
# Then, after the loop raise the exception group.

a_list = ["6", "foo", "nope", "54", "bar"]

result = []

try:
    caught_exceptions = []
    pass  # Your code
except* ValueError as eg:
    assert len(eg.exceptions) == 3
    print("Exception group is ok")
else:
    assert False, "No exception group raised"

assert result == [6, -1, -1, 54, -1]
print("results OK")
