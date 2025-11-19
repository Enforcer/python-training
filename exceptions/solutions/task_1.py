a_list = ["1", "7", "nope", "213"]

result = []

for el in a_list:
    try:
        result.append(int(el))
    except ValueError:
        result.append(-1)

assert result == [1, 7, -1, 213]
print("OK")
