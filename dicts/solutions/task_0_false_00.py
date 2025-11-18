# Create a dictionary where you will store different values for the following keys:
# 0
# 0.0
# False
# print the dict
# *Figure out a way how you can transform the keys so that you can store three different values under three different keys

a_dict = {
    0: "zero int",
    0.0: "zero float",
    False: "False"
}

print(a_dict)
print(len(a_dict))
print(hash(0), hash(0.0), hash(False))
print(0 == 0.0 == False)

a_dict_2 = {
    "0": "zero int",
    "0.0": "zero float",
    "False": "False"
}
print(a_dict_2)
assert len(a_dict_2) == 3
print("OK")
