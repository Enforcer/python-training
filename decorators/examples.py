# Simplest example
def decorator(fun):
    print(fun)  # will execute during interpreting 'fun'
    return fun


@decorator
def my_function(a, b):
    pass


# '@' is just a syntactic sugar
def another_fun(a, b): pass

another_fun = decorator(another_fun)

# is equivalent to

@decorator
def another_fun(a, b): pass


# More complex example
def double_result(fun):
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result * 2

    return new_fun


@double_result
def add(a, b):
    return a + b


add(1, 2)  # 6
add  # <function double_result.<locals>.new_fun at 0x107ea1c70>


# Make new function look like the original
from functools import wraps


def double_result_2(fun):
    @wraps(fun)  # < copies name from fun to new_fun
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        return result * 2
    return new_fun


@double_result_2
def add(a, b):
    return a + b

add  # <function add at 0x107ea1e80>


# Decorators factories
from functools import wraps


def multiply_result(how_many_times):
    def _multiply_result(fun):
        @wraps(fun)  # < copies name from fun to new_fun
        def new_fun(*args, **kwargs):
            result = fun(*args, **kwargs)
            return result * how_many_times
        return new_fun
    return _multiply_result


@multiply_result(3)
def add(a, b):
    return a + b
