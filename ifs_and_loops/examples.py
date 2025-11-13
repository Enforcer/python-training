# if [elif] [else]

a_list = [1, 2]

if len(a_list) == 2:
    print("OK")

# chaining
if len(a_list) % 2 == 0:
    print("Even number of elements")
elif len(a_list) % 2 == 1:
    print("Odd number of elements")
else:
    print("Impossible!")  # dead code

# walrus operator
a_dict = {}
if a_dict.get("name"):
    name = a_dict["name"]

# forbidden
# if name = a_dict.get("name"):
#    name = a_dict["name"]

if name := a_dict.get("name"):
    name = a_dict["name"]

# walrus operator - more complex example
if (modulo_2 := len(a_list) % 2) == 0:
    print("Even number of elements")
elif modulo_2 == 1:
    print("Odd number of elements")
else:
    print("Impossible!")  # dead code

# While loop
a_set = {1, 2, 3}
while a_set:
    removed_element = a_set.pop()
    print("removed_element:", removed_element)

# For loop
a_string = "Python"
for letter in a_string:
    print(letter)

# Control statements
for letter in ("a", "b", "c"):
    if letter == "a":
        continue # skip to the next iteration
    if letter == "c":
        break  # stop loop immediately
    print(letter)

# Unpacking in a loop
a_list_of_tuples = [("a", 1), ("b", 2)]
for letter, number in a_list_of_tuples:
    print(letter, number)

# Unpacking in a dict
a_dict = {"name": "Sebastian", "age": 18}
for key, value in a_dict.items():
    print(f"{key}={value}")

# For loop with enumeration
a_string = "Python"
for index, letter in enumerate(a_string):
    print(index, letter)  # 0 P, ...

# For loop with enumeration
a_string = "Python"
for index, letter in enumerate(a_string, start=1):
    print(index, letter)  # 1 P, ...

# Mutating sequence during iteration is forbidden
a_set = {1, 2, 3}
for element in a_set:
    print(f"Removing {element}")
    a_set.remove(element)  # RuntimeError: Set changed size during iteration
