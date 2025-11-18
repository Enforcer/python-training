from pydantic import BaseModel


class Measurement(BaseModel):
    temp: int
    name: str



measurement = Measurement(
    temp="123",  # gets converted to int!
    name="example",
)
print(repr(measurement))

