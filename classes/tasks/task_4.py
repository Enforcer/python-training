# Write a class hierarchy - Employee, SeniorEmployee and Executive, inheriting from each other:
# Employee <|-- SeniorEmployee <| -- Executive.
# Each class should have a following fields:
# - base_salary: int
# - tenure: int (years of working in a given place)
# Each class should define a method calculate_salary
# - Employee should just return a base_salary
# - SeniorEmployee should return whatever Employee returns (use super()) and add 100 for each year of tenure
# - Executive should return whatever SeniorEmployee returns (use super()) and add 10_000


assert Employee(1000, 1).calculate_salary() === 1000
assert SeniorEmployee(2000, 5).calculate_salary() == 2500
assert Executive(10_000, 10).calculate_salary() == 21000
print("OK")
