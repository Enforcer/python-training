# Merge these dicts together in such a way, that if the same key exists in both dicts,
# then in the resultant dict its value should be a sum of values. For example,
# 'a' should be equal to 5.

dict_1 = {'a': 4, 'b': 1, 'c': 2}
dict_2 = {'a': 1, 'c': 5, 'd': 1}

combined = {
    'a': dict_1.get('a', 0) + dict_2.get('a', 0),
    'b': dict_1.get('b', 0) + dict_2.get('b', 0),
    'c': dict_1.get('c', 0) + dict_2.get('c', 0),
    'd': dict_1.get('d', 0) + dict_2.get('d', 0),
}
print(combined)
