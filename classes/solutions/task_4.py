# Write a class hierarchy - Employee, SeniorEmployee and Executive, inheriting from each other:
# Employee <|-- SeniorEmployee <| -- Executive.
# Each class should have a following fields:
# - base_salary: int
# - tenure: int (years of working in a given place)
# Each class should define a method calculate_salary
# - Employee should just return a base_salary
# - SeniorEmployee should return whatever Employee returns (use super()) and add 100 for each year of tenure
# - Executive should return whatever SeniorEmployee returns (use super()) and add 10_000

class Employee:
    def __init__(self, base_salary: int, tenure: int) -> None:
        self._base_salary = base_salary
        self._tenure = tenure

    def calculate_salary(self) -> int:
        return self._base_salary

class SeniorEmployee(Employee):
    def calculate_salary(self) -> int:
        empl_salary = super().calculate_salary()
        return empl_salary + 100 * self._tenure

class Executive(SeniorEmployee):
    def calculate_salary(self) -> int:
        senior_empl_salary = super().calculate_salary()
        return senior_empl_salary + 10_000

assert Employee(1000, 1).calculate_salary() == 1000
assert SeniorEmployee(2000, 5).calculate_salary() == 2500
assert Executive(10_000, 10).calculate_salary() == 21000
print("OK")
