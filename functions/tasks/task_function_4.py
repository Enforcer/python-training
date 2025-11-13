# Given these two functions that can do different operations,
# write a third function - `calculate` that will accept three arguments:
# - a
# - b
# - operation
#
# `a` and `b` will be numbers and `operation` can be one of functions - `add` or `times`.


def add(a, b):
    return a + b


def times(a, b):
    return a * b


assert calculate(1, 1, add) == 2
assert calculate(2, 3, times) == 6
print("OK")
