# write a function `add_to_dict` that will accept a three arguments:
# - a dictionary
# - a key
# - a value
# The function will create a new dictionary (.copy() or dict comprehension) with `value` set under given `key`
# *if the key already exists in the dict, do nothing

a_dict = {"name": "Sebastian"}

...

result = add_to_dict(a_dict, "age", 18)

assert result is not a_dict  # ensure dict was copied
assert result == {"name": "Sebastian", "age": 18}
print("OK")
