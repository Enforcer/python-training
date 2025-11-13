# Find all the tasks files (.py inside tasks/) in this repository using Path.walk().
# Start from a given path.
# Once you find a tasks directory, print its parent - but do it only once.
import pathlib

this_file = pathlib.Path(__file__)
starting_point = this_file.parent.parent.parent  # repo root dir

print(starting_point)
