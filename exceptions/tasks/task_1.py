# Try converting items on the list in the loop, one at a time to integers (int()).
# When it fails, catch the appropriate exception and use -1

a_list = ["1", "7", "nope", "213"]

result = []

assert result == [1, 7, -1, 213]
print("OK")
