# defining sets
{"alpha", "bravo", "charlie"}
set(["alpha", "bravo", "charlie"])

set()  # the only way to create empty set

# fast element lookup
a_set = {"alpha", "bravo", "charlie"}
"delta" in a_set  # False
"bravo" in a_set  # True

# Adding elements (only if unique)
set_a = set()
set_a.add(1)  # set_a: {1}
set_a.add(1)  # set_a: {1}

# Element must be hashable
set([(1, 2, 3)])  # tuple consisting of immutable things is ok
set([[1, 2, 3]])  # this raises "unhashable type: 'list'"

# Adding multiple elements
set_a = set()
set_a.update([1, 2, 3])
set_a.update({4, 5, 6})

# Removing elements
set_a = set()
set_a.discard(1)  # Does nothing if element not in set
set_a.remove(1)  # Raises exception
{1, 2, 3}.pop()  # Remove 'random' element and return it, exception if set is empty

# union - combine unique elements
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a | set_b  # 1, 2, 3, 4
set_a.union(set_b)  # 1, 2, 3, 4

# intersection - element present in both sets
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a & set_b  # {2, 3}
set_a.intersection(set_b)

# difference
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a - set_b  # {1}
set_a.difference(set_b)

# symmetric difference
set_a = {1, 2, 3}
set_b = {2, 3, 4}
set_a ^ set_b  # {1, 4}
set_a.symmetric_difference(set_b)  # {1, 4}

# Other operations
{1, 2, 3}.isdisjoint({4, 5})  # True, no common elements
{1, 2, 3}.issuperset({2})  # True, {2} present in first set
{1, 2, 3}.issubset({2})  # False, {2} present in first set
