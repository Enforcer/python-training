# defining tuple
(1, 2, 3)
tuple([1, 2])
()
tuple()

# single-element tuple
(1)  # 1, NOPE
(1,)
1,

# length of a tuple
len((1, 2, 3))  # 3

# indexing 0..len() - 1
a_tuple = (1, 2, 3)
a_tuple[0]  # 1

# combining
(1, 2, 3) + (4, 5, 6)  # creates a new tuple

# slices
# [start:end:step] # all optional
(1, 2, 3)[1:-1]  # from 2nd to penultimate element, excluding it (2, )
