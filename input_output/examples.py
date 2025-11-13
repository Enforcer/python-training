# Accepting input from user - returns string
input("(Here goes your prompt!) Enter value: ")  # enter 123
# '123'

# Writing and reading standard output, standard error output and standard input
import sys

sys.stdout
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

sys.stdout.write("test\n")  # returns number of bytes written, 5
sys.stderr.write("error test\n")  # likewise, 11

sys.stdin
# <_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>
sys.stdin.read()  # will block until given EOL (CTRL+D)

# print - write to other 'file'
import sys


print("HEY")  # writes to stdout by default
print("HEY", file=sys.stderr)

# Opening files
file_name = "multi_line_file"
open(file_name)

# access mode
# "r" - read, error if file does not exist (default)
# "a" - append, creates file if not exist
# "w" - write, creates file if not exist
# "x" - creates the file, error if file does not exist

# text or binary?
# "t" - read str (default)
# "b" - read bytes

open("multi_line_file", "rb")  # read binary
open("multi_line_file", "w")  # write text

# Opening file for writing using context manager
with open("/tmp/a_file", "w") as f:
    f.write("Hello, world!")


# Manual operations on files
f = open("/tmp/a_file", "w")
f.write("Hello, world!")
f.close()
f.write("Hello, world!")  # raises ValueError: I/O operation on closed file

# pathlib
import pathlib

path = pathlib.Path("example_file")
path.write_text("example text")
# path.write_bytes()

path.exists()  # True
path.read_text()  # 'example text'
path.read_bytes()  # b'example text'

# Using open
with path.open() as f:
    print(f.read())

# Removing files
path.unlink()

# Directories
directory = pathlib.Path.cwd()
parent_dir = directory.parent

directory_with_this_file = directory / "input_output"

for root, directories, files in directory_with_this_file.walk():
    print(root, directories, files)


# Temporary files
import tempfile

with tempfile.TemporaryFile('r+') as f:  # read and write mode
    f.write('test')
    f.seek(0)
    print(f.read())
