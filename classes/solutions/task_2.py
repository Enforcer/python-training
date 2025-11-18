# Define an abstract base class Shape with one abstract method - area.
# Define two concrete subclasses, Rectangle and Square.
# Write appropriate __init__ for these classes and overload area method, code calculations and return results
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> int:
        pass


class Square(Shape):
    def __init__(self, side: int) -> None:
        self._side = side

    def area(self) -> int:
        return self._side**2


class Rectangle(Shape):
    def __init__(self, a: int, b: int) -> None:
        self._a = a
        self._b = b

    def area(self) -> int:
        return self._a * self._b


assert Square(4).area() == 16
assert Rectangle(4, 2).area() == 8
print("OK")
