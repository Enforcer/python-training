# Write a decorator called `log_call`.
# It should print a message like "Decorating function foo" when is applied.
# It should also print a message "Calling foo with arguments ..." and print those arguments.
from functools import wraps

def log_call(fun):
    print(f"I'm decorating {fun}")

    @wraps(fun)
    def wrapped(*args, **kwargs):
        print(f"Calling {fun} with {args} {kwargs}")
        return fun(*args, **kwargs)
    return wrapped

print("Interpreting - before foo")

@log_call
def foo(my_argument, *args):
    pass

print("Interpreting - after foo")

foo("example", 1, 2)
