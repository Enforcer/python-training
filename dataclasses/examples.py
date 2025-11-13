# Define dataclass
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

person = Person("Sebastian", 18)
print(person)

# Default values
from dataclasses import dataclass, field


@dataclass
class Person:
    name: str
    age: int = field(default=18)
    skills: dict[str, int] = field(default_factory=dict)


person = Person("Sebastian")
print(person)

# Immutability
from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str

person = Person(name="Sebastian")
## safe to use with dicts and sets
{Person(name="Sebastian"), Person(name="Sebastian")}
# {Person(name='Sebastian')}

person.name = "Jadwiga"  # raises exception

# __post_init__
from dataclasses import dataclass


@dataclass
class Money:
    amount: int
    currency: str

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Invalid amount")
        if self.currency not in ("USD", "PLN"):
            raise ValueError("Invalid currency")


money = Money(1, "PLN")
money = Money(-100, "PLN")
money = Money(1, "EUR")
