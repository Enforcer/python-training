"a string"

'a string'
"""
a string
"""
'''
a string
'''

# length of a string
len("a string")  # 8

# indexing 0..len() - 1
"a string"[2]  # s
"a string".index("s")  # 2
"a string".index("tr")  # 3

# combining
"a string" + " " + "another string"

# joining
" ".join(["Ala", "ma", "kota"])

# counting elements by value
"my oh my".count("m")  # 2
"my oh my".count("my")  # 2

# slices
# [start:end:step] # all optional
"foo"[:2]  # up to second element (stop before 3rd element) "fo"
"foo"[:-1]  # up to first element from the end, "fo"
"foo"[1:]  # start from second element 'oo'
"banana"[::2]  # every second element 'bnn'
"banana"[1::2] # 'aaa'


# immutable!
a_string = "a string"
a_string[0] = "b"  # TypeError
a_string[0:2] = "ab"  # TypeError

# reversing a string
"kajak"[::-1]
a_string = "a string"
a_string == a_string[::-1]  # is palindrome?
"abcdef"[::-1]  # 'fedcba'

# Selected methods
"string".endswith("s")
"string".startswith("s")
"string".capitalize()  # 'String'
"python".isdigit()  # False
"123".isdigit()  # True

"STRING".lower()  # "string"
'string'.upper()  # 'STRING'

"a long sentence".split(" ")  # ['a', 'long', 'sentence']
"COLUMN 1;COLUMN 2".partition(";")  # ('COLUMN 1', ';', 'COLUMN 2')
"COLUMN 1;COLUMN 2;COLUMN 3".partition(";")  # ('COLUMN 1', ';', 'COLUMN 2;COLUMN 3')
"COLUMN 1 COLUMN 2".partition(";")  # ('COLUMN 1 COLUMN 2', '', '')
"COLUMN 1 COLUMN 2".replace(" ", "_")  # 'COLUMN_1_COLUMN_2'
