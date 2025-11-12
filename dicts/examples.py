# defining dicts
{"key": "value", "another": 2}
dict(key="value", another=2)
dict([('key', 'value'), ('another', 2)])

{}
dict()

# assignment, retrieval, removal
a_dict = {}
a_dict["name"] = "Sebastian"
a_dict["name"]  # "Sebastian"
del a_dict["name"]
a_dict["name"]  # raises KeyError, dict is now empty
a_dict.get("name")  # None
a_dict.get("name", "UNKOWN")  # "UNKOWN"

# keys, values and both
a_dict = {"name": "Sebastian", "main_lang": "Python"}
a_dict.keys()  # dict_keys(['name', 'main_lang'])
list(a_dict)  # ['name', 'main_lang']
list(a_dict.keys())  # ['name', 'main_lang']

list(a_dict.values())  # ['Sebastian', 'Python']

# tuples (key, value)
list(a_dict.items())  # [('name', 'Sebastian'), ('main_lang', 'Python')]

# Combining dicts
one_dict = {"name": "Sebastian"}
another_dict = {"main_lang": "Python"}
dict(one_dict, **another_dict)
{**one_dict, **another_dict}
one_dict.update(another_dict)  # modify one dict with items from another one

# Special dict subclasses
## Counter
from collections import Counter

counter = Counter("dcaad")  # Counter({'d': 2, 'a': 2, 'c': 1})
# most common element and number of occurrences
counter.most_common(1)  # [('d', 2)] (one of most common)
counter = Counter({1, 2, 3})  # ?

## defaultdict
from collections import defaultdict

a_dict = defaultdict(list)  # function passed as an argument
a_dict["participants"].append("Sebastian")
print(a_dict)  # defaultdict(<class 'list'>, {'participants': ['Sebastian']})
