# Basic construction
try:
    1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


# multiple except blocks + else
raw_dividend = input("Enter dividend: ").strip()
raw_divisor = input("Enter divisor: ").strip()
try:
    dividend = int(raw_dividend)
    divisor = int(raw_divisor)
    result = dividend / divisor
except ValueError as exc:
    print("Conversion error: ", exc)
except ZeroDivisionError as exc:
    print("Can't divide by zero: ", exc)
else:
    print("Result is", result)


# Handling multiple exceptions classes
raw_dividend = input("Enter dividend: ").strip()
raw_divisor = input("Enter divisor: ").strip()
try:
    dividend = int(raw_dividend)
    divisor = int(raw_divisor)
    result = dividend / divisor
except (ValueError, ZeroDivisionError) as exc:
    print("Something is wrong: ", exc)
else:
    print("Result is", result)


# finally
from _typeshed import ExcInfo
import io
from multiprocessing import Value


f = open("multi_line_file", "r")
try:
    print("trying to write...")
    f.write("gibberish")
except io.UnsupportedOperation:
    print("writing failed")
finally:
    print("closing file")
    f.close()


# Catching all - don't do this at home
try:
    1 / 0
except:
    print("Failed")


# Reraising
try:
    1 / 0
except Exception as exc:
    print("Failed", exc)
    raise

# altogether
try:
    1 / 0
except ZeroDivisionError as exc:
    print("Can't divide by zero!")
else:
    print("it's fine")
finally:
    print("finalization")


# Handling exceptions in hierarchy
try:
    1 / 0
except Exception:
    print("oh shooot")
except ArithmeticError:
    # dead code, Exception is more general
    print("Arithmetic Error")
except ZeroDivisionError:
    # even more dead code
    # ZeroDivisionError inherits from ArithmeticError
    print("ZeroDivisionError")


# raising exceptions
try:
    raise ValueError
except ValueError as exc:
    print(f"Got {type(exc)} {exc}")


# raising exceptions with arguments
try:
    raise ValueError("Bad argument")
except ValueError as exc:
    print(f"Got {type(exc)} {exc}")


# Instantiating exceptions - variations with arguments
Exception  # none
Exception()  # none
Exception("Bad type")  # just error message
Exception("Bad type", int, 1)  # arbitrary number

# Access to arguments
exc1 = Exception()
print(exc1.args)
# ()

exc2 = Exception("Bad type", int, 1)
print(exc2.args)
# ('Bad type', <class 'int'>, 1)


# Custom exceptions
class MyException(Exception):
    pass

class WrongArgument(MyException):
    pass

class InvalidNumber(WrongArgument):
    pass


# Exception groups
exception_group = ExceptionGroup(
    "validation errors",
    [TypeError("str"), ValueError("at is not valid integer")]
)

# Exception group is an exception...
isinstance(exception_group, Exception)
# True

# ...hence can be caught
try:
    raise ExceptionGroup(
        "validation errors",
        [TypeError("str"), ValueError("at is not valid integer")]
    )
except Exception:
    print("Oh, no")


# Handling exceptions in the group - separate handlers
try:
    raise ExceptionGroup(
        "demo", [TypeError("bar"), ValueError("foo")]
    )
except* TypeError as eg:
    print(eg.exceptions)
except* ValueError as eg:
    print(eg.exceptions)


# Multiple exceptions of same type
try:
    raise ExceptionGroup(
        "demo", [TypeError("bar"), TypeError("baz")]
    )
except* TypeError as eg:
    print(eg.exceptions)
    # (TypeError('bar'), TypeError('baz'))


# Unhandled exceptions in group will bubble up
try:
    raise ExceptionGroup(
        "demo", [TypeError("bar"), ValueError("foo")]
    )
except* ValueError as eg:
    print(eg.exceptions)

# + Exception Group Traceback (most recent call last):
# |   File "<python-input-24>", line 3, in <module>
# |     raise ExceptionGroup(
# |         "demo", [TypeError("bar"), ValueError("foo")]
# |     )
# | ExceptionGroup: demo (1 sub-exception)
# +-+---------------- 1 ----------------
#   | TypeError: bar
#   +------------------------------------

# forbidden, can't have both except* and except
# in one try..except block
try:
    raise ExceptionGroup(
        "demo", [TypeError("bar"), ValueError("foo")]
    )
except* ValueError as eg:
    print(eg.exceptions)
except Exception as exc:
    print("Catch-all")


# ...but nesting is allowed
# only unconsumed exceptions are propagated
try:
    try:
        raise ExceptionGroup(
            "demo", [TypeError("bar"), ValueError("foo")]
        )
    except* ValueError as eg:
        print(eg.exceptions)
except Exception as exc:
    print("Catch-all", exc.args)
    # Catch-all ('demo', [TypeError('bar')])
