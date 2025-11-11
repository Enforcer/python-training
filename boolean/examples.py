# singletons
True
False

# Compare object identifier
id(True) == id(1 == 1)

# Comparing values
1 == 1

# Comparing identity
(1 == 1) is True

# Truthy values
bool([1, 2, 3])  # non-empty collection
bool("a string")  # non-empty string
bool(1)  # non-zero integers
bool(-1)

# Falsy values
bool([])  # empty collections
bool("")  # empty strings
bool(0)  # zero
0 == False  # should've used 'is', '==' considered non-idiomatic

# Operators
True and True  # True
True and False  # False
False or False  # False
False or True   # True

# Exclusive or
True ^ False  # True
True ^ True  # False
