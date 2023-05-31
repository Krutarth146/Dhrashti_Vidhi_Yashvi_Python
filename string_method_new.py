str1 = 'K'
print(type(str1))   # <class 'str'>

str2 = "Shrey_k"
print(str2)  # Shrey k

print(type(str2))   # <class 'str'>

print(len(str2))   # 7  -> Length starts from 1, Index starts from 0


# Indexing
print(str2[1])   # h
print(str2[-2])   # _

# Slicing
print(str2[2:5:1])    # rey
print(str2[-3:-6:-1])  # yer

str3 = "Royal_is Best Institute Ever123."
print(str3[-3:4:1])  # blank


print(str3[-3:4:-1])   # 21revE etutitsnI tseB si_

print(str3[-8:-2:-3])  # blank

print(str3[-2:-8:-3])   # 32

print(str3[::2])   # Ryli etIsiueEe13
print(str3[::-1])   # .321revE etutitsnI tseB si_layoR
print(str3[:0:-1])  # .321revE etutitsnI tseB si_layo
print(str3[:-5:-1])  # .321


# String Methods
str3 = "Royal_Is Best Institute Ever123."

print(str3.capitalize())   # Royal_is best institute ever123.
print(str3.casefold())   # royal_is best institute ever123.
print(str3.swapcase())   # rOYAL_IS bEST iNSTITUTE eVER123.
print(str3.upper())   # ROYAL_IS BEST INSTITUTE EVER123.
print(str3.lower())   # royal_is best institute ever123.
print(str3.title())   # Royal_Is Best Institute Ever123.
print(str3.istitle())   # True
print(str3.islower())   # False
print(str3.isupper())   # False
print(str3.isspace())   # False



str3 = "Royal Is Best Institute Ever123."

print(str3.split(' '))   # ['Royal_Is', 'Best', 'Institute', 'Ever123.']

print(str3.partition(' '))   # ('Royal_Is', ' ', 'Best Institute Ever123.')  -> Divides into 3 parts
print(str3[8:].partition(' '))   # ('', ' ', 'Best Institute Ever123.')


'''
Tasks in tuple -: 

1. Python program to find the size of a tuple
-> tuple = ("python", "includehelp", 43, 54.23)

2. Python program for adding a Tuple to List and Vice-Versa
-> tuple = ("python", "includehelp", 43, 54.23)

3. Python program to find the maximum and minimum K elements in a tuple
-> 
Input: 
myTuple = (4, 2, 5,7, 1, 8, 9), k = 2

Output: 
(9, 8) , (1, 2)

4. Python program to create a list of tuples from given list having number and its cube in each tuple
->
Input: 
list = [4, 1, 6, 2]

Output: 
[(4, 64), (1, 1), (6, 216), (2, 8)]

5. Python program to remove all tuples of length K
-> 
Input:
[(1, 4), (2), (4,5,6,8), (26), (3, 0, 1), (4)] k = 1

Output:
[(1, 4), (4, 5, 6, 8), (3, 0, 1)]

6. Python program to extract digits from tuple list
->
Input: 
list = [(4, 62), (2, 65), (5, 9), (0,1)]

Output:
[4, 6, 2, 5, 9, 0, 1]

7. Python program to find all pairs combination of two tuples
->
Input:
tup1 = (1, 2), tup2 = (5, 7)

Output:
[(1, 5), (1, 7), (2, 5), (2, 7), (5, 1), (5, 2), (7, 1), (7, 2)]

8. Python program to join tuples if similar initial element
->
Input:
list = [(1, 4), (3, 1), (1, 2), (4, 2), (3, 5)]

Output:
list = [(1, 4, 2), (3, 1, 5), (4, 2)]

9. Python program to sort a list of tuples by second item
->
Input:
[(2, 5), (9, 1), (4, 6), (2, 8), (1, 7)]

Output:
[(9, 1), (2, 5), (4, 6), (1, 7), (2, 8)]

10. Python program to sort a list of tuples in increasing order by the last element in each tuple
-> tupList =[(5, 7), (12, 4), (20, 13), (45, 2)]

11. Python program to sort tuples by frequency of their absolute difference
-> 
Input:
[(4,6), (1, 3), (6, 8), (4, 1), (5, 2)]

Output:
[(4, 1), (5, 2), (4, 6), (1, 3), (6, 8)]

12. Python program to remove duplicate tuples irrespective of order
->
Input:
tupList = [(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

Output:
[(3, 1), (5, 8), (1, 3), (4, 8), (2, 9)]

13. Python program to order tuples by list
->
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]

14. Python program to concatenate maximum tuples
->
Input:
tupList = [("python", 7), ("learn" , 1), ("programming", 7), ("code" , 3)]

Output:
"python programming"

15. Python program to flatten tuple of lists to a tuple
->
Input:
([4, 9, 1], [5 ,6])

Output:
(4, 9, 1, 5, 6)
'''