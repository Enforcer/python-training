# Create a dict that will be mapping name to the following structure:
# {"points": 7, "hits": 12, "misses": 5}
#
# You should take care to initialize the structure with 0s when a given key is first referenced:
# {"points": 0, "hits": 0, "misses": 0}
#
# Use a lambda function to achieve desired result
from collections import defaultdict

a_dict = ...


assert a_dict["NameForTheFirstTime"] == {"points": 0, "hits": 0, "misses": 0}
a_dict["AnotherName"]["points"] += 1
a_dict["AnotherName"]["hits"] += 1
print("OK")
