# Find all the tasks files (.py inside tasks/) in this repository using Path.walk().
# Start from a given path.
# Once you find a tasks directory, print its parent - but do it only once.
import pathlib


this_file = pathlib.Path(__file__)
starting_point = this_file.parent.parent.parent  # repo root dir


print(f"Starting from: {starting_point}")


for root, directories, files in starting_point.walk():
    if str(root).endswith("/tasks"):
        print(f"Found catalog with tasks: {root}")

        for file in files:
            if str(file).endswith(".py"):
                print(f"  {file}")
