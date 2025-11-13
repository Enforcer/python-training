# Write a function `joiner` that will be accepting:
# - a string
# - a variadic number of arguments
# and will use a passed string as a separator - then returns the result.
# If the passed string is empty ("") or no extra arguments were passed, then return immediately just the empty string.
#
# Example usage: "|".join(["one", "two"])  # "one|two"
#
# *Convert elements of variadic arguments to strings so it can also work with e.g. integers

assert function(",", "a", "b") == "a,b"
assert function("") == ""
print("OK, basic part")
assert function("|", 1, 2) == "1|2"
print("OK, advanced part")
