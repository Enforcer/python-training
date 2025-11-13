# Basic construction
try:
    1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")


# multiple except blocks + else
raw_dividend = input("Enter dividend: ")
raw_divisor = input("Enter divisor: ")
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


# finally
import io


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
