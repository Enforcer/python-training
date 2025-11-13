# Example
with open("multi_line_file") as f:  # <-- context manager
    pass

# Basic definition

class ContextManager:
    def __enter__(self) -> None:
        print("Entering")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting")


context_manager = ContextManager()

with context_manager:
    print("Inside")

# Entering
# Inside
# Exiting

# Modern approach with functions
from contextlib import contextmanager


@contextmanager
def context_manager():
    print("Entering")
    yield
    print("Existing")


with context_manager():
    print("Inside")

# Entering
# Inside
# Existing
