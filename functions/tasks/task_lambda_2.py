# Use lambda function passed to list's sort to ensure strings are sorted from the shortest to the longet


strings = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua']

# sort


assert len(strings[0]) == 2
assert len(strings[-1]) == 11
print("OK")
