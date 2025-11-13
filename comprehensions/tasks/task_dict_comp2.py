# Filter out only people that have at least one point and create a new dict,
# where values will be string 'POINT'.
# Use one dict comprehension to do it all.

scoreboard = {
    "Sebastian": 0,
    "Jacek": 0,
    "Agatka": 1,
    "Marcelina": 1,
    "Krzysztof": 0,
    "Bartek": 1
}

a_dict = {}

assert a_dict == {'Agatka': 'POINT', 'Marcelina': 'POINT', 'Bartek': 'POINT'}
print("OK")
