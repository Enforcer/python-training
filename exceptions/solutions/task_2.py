import io


file = open("some_file", "r")
try:
    file.write("string")
except io.UnsupportedOperation:
    print("Oups, shouldn't have done that :o")
finally:
    file.close()


try:
    file.read()
except ValueError:
    print("That failed as expected")
