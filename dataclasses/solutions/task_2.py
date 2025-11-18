# Create a dataclass named Point with two fields: x and y, both of type float
# Make it immutable by setting frozen attribute in @dataclass decorator.
# Create a few instances and add them to a set - repeatedly to ensure they are deduplicated.
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(2.0, 2.0)

a_set = set()

a_set.add(p1)
a_set.add(p1)
a_set.add(p1)
a_set.add(p2)
a_set.add(p2)
print(a_set)
assert len(a_set) == 2
print("OK")
