# Modify the fibonacci() generator example so that it takes a `max_value` argument.
# It shoud only yields numbers up to that maximum value before stopping.
# Use an if condition and return or stop the loop using break
def fibonacci(limit) -> Iterator[int]:
    a, b = 0, 1
    while True:
        if a > limit:
            break
        yield a
        a, b = b, a + b


print(list(fibonacci(limit=8)))
