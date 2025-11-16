# defining list
[1, 2, 3]
# list(another_object)
list("Sebastian")
# ['S', 'e', 'b', 'a', 's', 't', 'i', 'a', 'n']

# starting with empty list
[]
list()

# length of a list
len([1, 2, 3])  # 3
len([])  # ?

# indexing 0..len() - 1
a_list = [1, 2, 3]
a_list[0]  # 1
a_list.index(1)  # 0
a_list = [1, 2, 3, 3, 3, 3]
a_list.index(3)  # ?

# combining
[1, 2, 3] + [4, 5, 6]  # creates new list
a_list = [1, 2, 3]
a_list.extend([3, 3, 3])  # extends original list

# counting elements by value
a_list.count(4)

# slices
# [start:end:step] # all optional
[1, 2, 3][:2]  # up to second element (stop before 3rd element)
[1, 2, 3][:-2] # up to second element from the end, [1]
[1, 2, 3][1:]  # start from second element
[1, 2, 3][::2]  # every second element
[1, 2, 3][1::2]

a_list = [1, 2, 3]
a_list[0:2] = [0, 0]  # [0, 0, 3]

# reversing a list
[1, 2, 3][::-1]  # ?

# copying
a_list = [1, 2, 3]
another_list = a_list.copy()
another_list[:]

# sorting
a_list = [3, 5, 1]
a_list.sort()  # in-place, [1, 3, 5]
sorted([3, 5, 1])  # copy

# unpacking
a, b, c = [1, 2, 3]
a, *rest = [1, 2, 3]
head, *middle, tail  = [1, 2, 2, 3]

# stack
# append, remove
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # 2

# queue
queue = []
queue.insert(0, 1)
queue.insert(0, 2)
queue.pop()  # 1

# Implementacja w pamieci

# Bad idea!
from collections import deque

queue = deque()
queue.appendleft(1)
queue.appendleft(2)
queue.pop()  # 1

# Check z timeit
# python3.14 -m timeit -s 'queue = []' 'queue.insert(0, 1)'

# python3.14 -m timeit -s 'from collections import deque; queue = deque()' 'queue.insert(0, 1)'

# Parę detali odnośnie implementacji w pamięci, zamortyzowany koszt
