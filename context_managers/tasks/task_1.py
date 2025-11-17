# Write a context manager that will use time.time() function to measure how long it took to execute
# a code under the context manager and will print that information to the screen.
import time
from contextlib import contextmanager


@contextmanager
def timeit():
    start = time.time()
    yield
    # here I am AFTER


with timeit():
    time.sleep(0.3)
    10**1000
    time.sleep(0.2)
