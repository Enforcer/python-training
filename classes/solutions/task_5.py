# Create a custom class inhriting from built-in list and write methods __eq__ and __hash__, based on value of first element of the list (self[0])
# Create an instance of such a custom type inheriting from list and try using it sets or in dicts as keys. See what happens


class EvilList(list):
    def __eq__(self, other) -> bool:
        return self[0] == other[0]

    def __hash__(self) -> int:
        return hash(self[0])

    def __str__(self) -> str:
        return f"I am Evil List, I'm using {self[0]} to represent myself ({self})"


el = EvilList([1, 2, 3])
print({el: 123})
print({el})
