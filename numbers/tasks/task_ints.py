# Calculate average of 3 numbers. It must not be float
a = 2
b = 3
c = 4

avg = a + b + c

assert type(avg) is int, "Average must be int!"
assert avg == 3
print("OK")
