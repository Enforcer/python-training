# Create a dataclass Result with two fields:
# - success - boolean type, default True
# - errors - list of strings, use default factory to ensure it will be properly initialized
# Create three instances:
# - one with success True and no errors
# - second one with success False and a list of errors
# - third one with success False and empty list of errors
# Add some errors to the list in case of third instance.
from dataclasses import dataclass, field

@dataclass
class Result:
    success: bool
    errors: list[str] = field(default_factory=lambda: list())


r1 = Result(success=True)
r2 = Result(success=False, errors=["memory overload"])
r3 = Result(success=False, errors=[])
r3.errors.append("Example 1")
r3.errors.append("Example 2")

print(r1)
print(r2)
print(r3)
