# Infinite generator
from typing import Iterator


def count() -> Iterator[int]:
    number = 1
    while True:
      yield number
      number += 1


for number in count():
    if number == 5:
        break
    print(number)

# fibonacci
def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


generator = fibonacci()
next(generator)  # 0
next(generator)  # 1
next(generator)  # 1
next(generator)  # 2
...

# Counting
from typing import Iterator

def numbers_up_to(maximum: int) -> Iterator[int]:
  number = 1
  while number <= maximum:
    yield number
    number += 1

for number in numbers_up_to(3):
  print(number)


# Built-in generator
for number in range(3):
    print(number)  # 0 1 2


# Counting with start and stop (exclusive) and step
for number in range(10, 15, 1):
    print(number)  # 10, 11, 12, 13, 14


# using iter() and next() on iterating-capable object
gen = iter(range(3))  # start iteration over generator
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # raises an exception StopIteration
