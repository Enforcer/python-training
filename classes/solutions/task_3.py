# Define two classes - Point and Segment.
# Point should consist of two fields - x and y coordinates.
# Segment should consist of two points - a and b.
#
# Add __len__ dunder method to Segment that will calculate length of the Segment.
# The formula is math.sqrt((point_2.x - point_1.x)**2 + (point_2.y - point_1.y)**2)
import math


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Segment:
    def __init__(self, a: Point, b: Point) -> None:
        self.a = a
        self.b = b

    def __len__(self) -> int:
        return int(math.sqrt((self.b.x - self.a.x)**2 + (self.b.y - self.a.y)**2))


segment = Segment(
    Point(0, 0),
    Point(0, 10),
)
assert len(segment) == 10
print("OK")
