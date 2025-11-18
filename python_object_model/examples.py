# __new__
class Shy:
    counter = 0
    def __new__(cls):
        cls.counter += 1
        return int.__new__(int, cls.counter)


# __del__
class WithDel:
    def __del__(self):
        print("WithDel being finalized")

obj = WithDel()
del obj

def fun():
    print("fun - start")
    obj = WithDel()
    print("fun - end")


fun()
# fun - start
# I
# fun - end

# __repr__ and __str__
class Python:
    def __init__(self, version: str) -> None:
        self._version = version

    def __str__(self) -> str:
        return f"Python v{self._version}"

    def __repr__(self) -> str:
       return f'Python(version="{self._version}")'


python = Python(version="3.14"
print(str(python))  # Python v3.14
print(repr(python))  # Python(version="3.14")

>>> python  # interactive console
# Python(version="3.14")

# __hash__
just_a_set = {[1]}  # TypeError: cannot use 'list' as a set element (unhashable type: 'list')


class EvilList(list):
    def __hash__(self) -> int:
        return hash(self[0])

poisoned_set = {EvilList([1])}
print(poisoned_set)  # {[1]}

# __bool__
class TruthySetIfOnlyEvenNumbers(set):
    def __bool__(self) -> None:
        return all(isinstance(n, int) and n % 2 == 0 for n in self)


print(bool(TruthySetIfOnlyEvenNumbers([1, 2, 3])))  # False
print(bool(TruthySetIfOnlyEvenNumbers([0, 4])))  # True
