# Write a class Person that will have an attribute "_age".
# Add a property `age` for read-only access to that attribute
# Add a method called `age_me` that will increase `_age` by one each time it is called.

class Person:
    def __init__(self, age: int) -> None:
        self._age = age

    @property
    def age(self) -> int:
        return self._age

    def age_me(self) -> None:
        self._age += 1

person = Person(18)
assert person.age == 18
person.age_me()
person.age_me()
assert person.age == 20
print("OK")
