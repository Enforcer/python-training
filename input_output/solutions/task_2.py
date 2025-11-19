# Open a new file with name "example" in a write mode.
# Accept input from the user (input() function) and save it to the file _reversed_.
# Then close the file and open it again in read mode.
# Read the content and print it to the screen.

with open("example", "w") as f:
    data = input("Enter string: ")
    reversed = data[::-1]
    f.write(reversed)


with open("example") as f:
    data = f.read()
    print(data)
