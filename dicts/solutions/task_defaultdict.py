# Create an instance of defaultdict that will create lists for missing keys.
# Try appending a couple cities names to country keys, e.g. Poland - Warsaw, Wroclaw, Lodz or Germany - Koln, Berlin, Munchen
# DO NOT create lists under keys explicitly
# print the contents of the resultant dict

from collections import defaultdict

a_dict = defaultdict(list)
a_dict["Poland"].append("Warsaw")
a_dict["Poland"].append("Lodz")
a_dict["Poland"].append("Krakow")

a_dict = defaultdict(list)
a_dict["Germany"].append("Koln")
a_dict["Germany"].append("Berlin")
a_dict["Germany"].append("Munchen")

print(a_dict)
