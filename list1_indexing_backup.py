list1 = [10,20,30,40,5]
print(list1)  # [10, 20, 30, 40, 5]
print(type(list1))  # <class 'list'>

list2 = [10, 90.89, True, 90+8j, [2,3,4,5], (9,31,1,3), 'Y', 'Royal']
print(list2)  # [10, 90.89, True, (90+8j), [2, 3, 4, 5], (9, 31, 1, 3), 'Y', 'Royal']

# list -> characteristics: 
# List -> Ordered(Indexed) , Allows Duplicates, Mutable (Changeble)

list2 = [10, 90.89, True, 90+8j, [2,3,4,5], (9,31,1,3), 'Y', 'Royal', 10]
        # 0   1      2     3       4           5         6      7
   #    -8   -7     -6    -5      -4          -3         -2    -1
print(len(list2))  # 8  -> Length starts from 1, Index starts from 0
print(list2[0])   # 10

print(list2)  # [10, 90.89, True, (90+8j), [2, 3, 4, 5], (9, 31, 1, 3), 'Y', 'Royal', 10]
print(list2[-1])   # Royal
print(list2[4])  # [2,3,4,5]

print(list2.__sizeof__())   # 112


# List Indexing: --------
print(list2[6])  # Y

# List Slicing
# print(list2[start : end(n-1)])

print(list2[0 : 6])  # start - 0, end = 5  # [10, 90.89, True, (90+8j), [2, 3, 4, 5], (9, 31, 1, 3)]


list2 = [10, 90.89, True, 90+8j, [2,3,4,5], (9,31,1,3), 'Y', 'Royal', 10]
print(list2[3:5])  # [(90+8j), [2, 3, 4, 5]]
print(list2[3:4])  # [(90+8j)]
print(list2[3:3])  # []
print(list2[3:])  # [(90+8j), [2, 3, 4, 5], (9, 31, 1, 3), 'Y', 'Royal', 10]
print(list2[:5])  # [10, 90.89, True, (90+8j), [2, 3, 4, 5]]
print(list2[:])   # [10, 90.89, True, (90+8j), [2, 3, 4, 5], (9, 31, 1, 3), 'Y', 'Royal', 10]

print(list2[5:1])  # []

# print(list2[start:end(n-1):step(n-1)])
print(list2[2:8:1])  # [True, (90+8j), [2, 3, 4, 5], (9, 31, 1, 3), 'Y', 'Royal']
list2 = [10, 90.89, True, 90+8j, [2,3,4,5], (9,31,1,3), 'Y', 'Royal', 10]
print(list2[3:7:2])  # [(90+8j), (9, 31, 1, 3)]
print(list2[3::2])  # [(90+8j), (9, 31, 1, 3), 'Royal']
print(list2[::3])  # [10, (90+8j), 'Y']


list2 = [10, 90.89, True, 90+8j, [2,3,4,5], (9,31,1,3), 'Y', 'Royal', 10]
print(list2[3:8:-1])  # []
print(list2[8:3:-1])  # [10, 'Royal', 'Y', (9, 31, 1, 3), [2, 3, 4, 5]]
print(list2[6::-2])  # ['Y', [2, 3, 4, 5], True, 10]
print(list2[::-3])   # [10, (9, 31, 1, 3), True]
print(list2[::-1])  # [10, 'Royal', 'Y', (9, 31, 1, 3), [2, 3, 4, 5], (90+8j), True, 90.89, 10]
print(list2[-2:-7:-2]) # ['Royal', (9, 31, 1, 3), (90+8j)]