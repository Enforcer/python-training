# List comprehension - map
a_list = [1, 2, 3]
[element**2 for element in a_list]  # list of squares

# List comprehension - filter
a_list = [1, 2, 3]
[element for element in a_list if element % 2 == 0]  # list of squares

# List comprehension - combined
[element**2 for element in a_list if element % 2 == 0]

# Set comprehension
a_string = "Python"
unique_lowercase_letters = {letter for letter in a_string if letter.islower()}

# Dict comprehension
members = ["Jack", "Agatha"]
{name: 0 for name in members}  # {'Jack': 0, 'Agatha': 0}

a_string = "Python"
letters_are_lower = {letter: letter.islower() for letter in a_string}
# {'P': False, 'y': True, 't': True, 'h': True, 'o': True, 'n': True}
