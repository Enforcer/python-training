# Defining custom type
class MyClass:
    CLASS_ATTRIBUTE = 123

    def foo(self) -> None:
        pass


# Dunder methods (AKA special/magic methods)
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        """Called when doing str(object)"""
        return "Person(" + self.name + ", " + str(self.age) + ")"


person = Person("Sebastian", 18)
person.name  # "Sebastian"
person.age  # 18
print(person)  # __str__: 'Person(Sebastian, 18)'


# Attributes resolution order
class Example:
    attribute = "class-level attribute"


print(Example.attribute)  # "class-level attribute"
example = Example()
print(example.attribute)  # "class-level attribute"
example.attribute = "instance-level attribute"
print(example.attribute)  # "instance-level attribute"

print(example.__dict__)
# {'attribute': 'instance-level attribute'}

print(Example.__dict__)


# Classmethod
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def adult(cls, name: str) -> "Person":
        return Person(name, 18)


Person.adult("Sebastian").age  # 18


# Staticmethod
class YetAnotherClass:
    @staticmethod
    def uppercase(a_string: str) -> str:
        return a_string.upper()


YetAnotherClass.uppercase("python")  # PYTHON


# Operators overloading
class Config:
    def __init__(self, **kwargs: int) -> None:
        self._config = kwargs.copy()

    def __getitem__(self, key: str) -> None:
        """To support object[key]"""
        return self._config[key]

    def __contains__(self, key: str) -> None:
        """To support key in object"""
        return key in self._config.keys()


config = Config(threads=123)
config["threads"]  # 123
"processes" in config  # False


# Using custom types in sets and as keys in dicts
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


one = Person("Sebastian", 18)
another = Person("Sebastian", 18)
points_by_person = {}
points_by_person[one] = 0
points_by_person[another] = 0
print(points_by_person)
# {<__main__.Person object at 0x1051a46e0>: 0, <__main__.Person object at 0x104fd2350>: 0}
print(set(points_by_person.keys()))
# {<__main__.Person object at 0x104fd2350>, <__main__.Person object at 0x1051a46e0>}

class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Person) and value.name == self.name

one = Person("Sebastian", 18)
another = Person("Sebastian", 18)
points_by_person = {}
points_by_person[one] = 0
points_by_person[another] = 0
print(points_by_person)
# {<__main__.Person object at 0x1051a4980>: 0}
print(set(points_by_person.keys()))
# {<__main__.Person object at 0x1051a4980>}

# Properties and "private" attributes
class Car:
    def __init__(self, mileage: int) -> None:
        self._mileage = mileage  # "private" by convention

    def _tamper_with_mileage(self, new_mileage: int) -> None:
        self._mileage = mileage

    @property
    def mileage(self) -> int:  # read-only
        return self._mileage

# Inheritance
class Person:
    pass

class Employee(Person):
    pass


# Inheritance - Calling __init__ or implementations from superclass in general
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name: str, age: int, role: str) -> None:
        super().__init__(name, age)  # must manually call superclass __init__
        self.role = role

# Multi-inheritance and Method Resolution Order
class Foo:
    def foo(self) -> None:
        print("Foo.foo")


class Bar:
    def foo(self) -> None:
        print("Bar.foo")


class Baz(Foo, Bar):
    pass


Baz().foo()  # Foo.foo


class Baz(Bar, Foo):
    pass


Baz().foo()  # Bar.foo


# Abstract classes
import abc


class Authentication(abc.ABC):
    @abc.abstractmethod
    def authenticate(self) -> bool:
        pass


Authentication()  # raises exception


class BasicAuth(Authentication):
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def authenticate(self) -> bool:
        return self.username == 'admin'
