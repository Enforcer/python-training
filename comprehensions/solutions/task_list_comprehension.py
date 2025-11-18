# Use list comprehension to create a list of numbers, raised to the power of 3

a_list = [1, 2, 3, 4, 5]
new_list = [number**3 for number in a_list]

assert new_list == [1, 8, 27, 64, 125]
print("OK")
