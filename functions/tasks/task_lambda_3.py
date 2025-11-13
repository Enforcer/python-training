# Sort the list of people from oldest to youngest using lambda passed list's sort() method.
# *In case of identical age, decide who goes first by comparing names alphabetically.

people = [
    {"name": "Alice", "age": 38},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 45},
    {"name": "Diana", "age": 19},
    {"name": "Evan", "age": 52},
    {"name": "Fiona", "age": 38},
    {"name": "George", "age": 60}
]

oldest = people[0]
assert oldest == {"name": "George", "age": 60}
youngest = people[-1]
assert youngest == {"name": "Diana", "age": 19}
print("OK, basic part")
assert people[3] == {'name': 'Alice', 'age': 38}
print("OK, advanced part")
