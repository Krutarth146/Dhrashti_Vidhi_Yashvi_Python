# int a[10] = {10,20,30,40};

list1 = []
print(type(list1))  # <class 'list'>

list2 = [10,10, 45.90, 'H', "Hetvi", True, [10,90,89], 8+9j, 10, 90]
print(list2)  # [10, 45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j)]
print(len(list2))   # 7 -> length starts from 1, Index starts from 0

# List characteristics -> Ordered (Indexed), Allow Duplicates, Mutable(Changeble)

# list2 = [10, 45.90, 'H', "Hetvi", True, [10,90,89], 8+9j]
#         0    1      2     3       4      5          6
#        -7     -6    -5    -4      -3     -2         -1


# Indexing ---------------------------------
print(list2[0])   # 10
print(list2[-1])   #  (8+9j)
print(list2[-4])   #  Hetvi
print(list2[2])   #  H

print(list2)  # [10, 10, 45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j), 10]


# Slicing ------------------------------------

# print(list1[start : end(n-1)])
print(list2[0 : 5])   # start - 0, End - 4  # [10, 10, 45.9, 'H', 'Hetvi']
print(list2[2 : 7])   # [45.9, 'H', 'Hetvi', True, [10, 90, 89]]
print(list2[2 : ])   # [45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j), 10, 90]
print(list2[ : 4])   # [10, 10, 45.9, 'H']
print(list2[ : ])   # [10, 10, 45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j), 10, 90]
print(list2[4 : 7])   # ['Hetvi', True, [10, 90, 89]]
print(list2[7 : 4])   # []


# [start : end(n-1) : step(n-1)]
print(list2[4 : 7 : 1])   # ['Hetvi', True, [10, 90, 89]]  by default
print(list2[0 : 7 : 2])   # [10, 45.9, 'Hetvi', [10, 90, 89]]
print(list2[0 : 7 : -1])   # []
print(list2[7 : 0 : -1])   # [10, 45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j)]
print(list2[4 : 5])   # ['Hetvi']
print(list2[-2:-6:-3])   # [10, True]
print(list2[2::])   # [45.9, 'H', 'Hetvi', True, [10, 90, 89], (8+9j), 10, 90]
print(list2[:7:])   # [10, 10, 45.9, 'H', 'Hetvi', True, [10, 90, 89]]
print(list2[:7:])   # [10, 10, 45.9, 'H', 'Hetvi', True, [10, 90, 89]]
print(list2[::3])   # [10, 'H', [10, 90, 89], 90]
print(list2[::-2])   # [90, (8+9j), True, 'H', 10]
print(list2[:5:-2])   # 


