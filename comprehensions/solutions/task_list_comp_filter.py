# Create another list of names, leaving only those that starts with (.startswith()) capital letter 'A'

a_list = ['Anastazja', 'Jacek', 'Agatka', 'Marcelina', 'Krzysztof', 'Bartek', 'Angelika']

another_list = [name for name in a_list if name.startswith("A")]

assert another_list == ['Anastazja', 'Agatka', 'Angelika']
print("OK")
