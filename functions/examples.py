# defining functions
def add(a, b):
    return a + b


# function definition with type annotations
def add(a: int, b: int) -> int:
    return a + b


# default arguments
def add(a: int, b: int = 1) -> int:
    return a + b

add(5)  # 6


# mutable default arguments
def append(element: int, to_what: list = []) -> list:
    to_what.append(element)
    return to_what


append(1, [])  # [1]
append(1)  # [1]
append(1)  # [1, 1]

# function with variadic argumets
def add(*numbers: int) -> int:
    total = 0
    for number in numbers:
        total += number
    return total

add(1, 2, 3, 5)  # 11

# accepts sequences unpacking
a_tuple = (1, 2, 3, 5)
add(*a_tuple)  # 11
a_list = [1, 2, 3, 5]
add(*a_list)  # 11

# function with named arguments
def configure(**options: int) -> None:
    for key, value in options.items():
        print(key, "=", value)

configure(threads=2, processes=4)
# threads = 2
# processes = 4

# accepts dicts unpacking
a_dict = {"threads": 2, "processes": 4}
configure(**a_dict)

# anonymous function, lambda
## Basics
f = lambda a, b: a + b
f(1, 2)  # 3

## Use case #1: defaultdict
from collections import defaultdict

trainings = defaultdict(lambda: set())
trainings["Sebastian"].add("Python training")

## Use case #2: sorting, by second element in a tuple
a_list_of_tuples = [("Jack", 44), ("Agatha", 52)]
a_list_of_tuples.sort(key=lambda element: element[1])
print(a_list_of_tuples)  # [('Jack', 44), ('Agatha', 52)]

# In reverse
a_list_of_tuples = [("Jack", 44), ("Agatha", 52)]
a_list_of_tuples.sort(key=lambda element: -element[1])
print(a_list_of_tuples)  # [('Agatha', 52), ('Jack', 44)]

# by first element in a tuple
a_list_of_tuples.sort(key=lambda element: element[0])
print(a_list_of_tuples)  # [('Agatha', 52), ('Jack', 44)]

# by multiple criteria
a_list_of_lists = [[1, 2, 3], [6], [5, 8]]
# sort first from the biggest sum of a nested list, then by number of elements from the smallest to the biggest
a_list_of_lists.sort(key=lambda element: (-sum(element), len(element)))
print(a_list_of_lists)  #
