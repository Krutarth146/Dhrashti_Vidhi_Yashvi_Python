str1 = 'RIshita'
str2 = "Y"

print(str1,str2,sep = '_')  # RIshita_Y

print(type(str1))  # <class 'str'>
print(type(str2))  # <class 'str'>


str1 = "Royal_is Best Institute Ever123."
print(len(str1))   # 32  -> Length starts from 1
print(str1[0])  # R
print(str1[-1])  # .

print(str1.capitalize())  # Royal is best institute ever123.
print(str1.casefold())    # royal is best institute ever123.
print(str1.lower())      # royal is best institute ever123.
print(str1.upper())      # ROYAL IS BEST INSTITUTE EVER123.
print(str1.swapcase())   # rOYAL IS bEST iNSTITUTE eVER123.
print(str1.title())      # Royal_Is Best Institute Ever123.

print(str1.index('Ever'))   # 24 -> index starts from 0
print(str1.index('.'))   # 31
print(str1.index('3.'))   # 30
print(str1.rindex('3.'))   # 30
print(str1.index('e'))   # 10
print(str1.rindex('e'))   # 26

print(str1.find('e'))  # 10
print(str1.find('Z'))  # -1  Returns -1 if element is Not Found
# print(str1.index('Z'))  # 10  Generates Error if element is Not Found


str1 = "Royal_is Best Institute Ever123."
print(str1.count('e'))  # 3
print(str1.count('ROyal'))  # 0
print(str1.count('layoR'))  # 0

print(str1[ : :-1])   # .321revE etutitsnI tseB si_layoR

print(str1)  # Royal_is Best Institute Ever123.


x = "_"

str2 = ' '.join(str1)
print(str2)  # R o y a l _ i s   B e s t   I n s t i t u t e   E v e r 1 2 3 .


print(str1.split('_'))   # ['Royal', 'is Best Institute Ever123.']
print(str1.split(' '))   # ['Royal_is', 'Best', 'Institute', 'Ever123.']


print(str1.partition(' '))  # ('Royal_is', ' ', 'Best Institute Ever123.')  # Divided into 3 parts Only
print(str1.rpartition(' '))  # ('Royal_is Best Institute', ' ', 'Ever123.')  # Divided into 3 parts Only


print(str1.replace('Institute', 'Technosoft'))  # Royal_is Best Technosoft Ever123.

str11 = "Keep yourself Mute while Not Speaking"
# ans = "Keep#yourself Mute while Not_Speaking"

print(str11.replace(' ','#',1))  # Keep#yourself Mute while Not Speaking




# String Programs

# 1. Write a Py program that takes your full Name and Print Like This :
# Input - Krutarth Daxeshbhai Patel
# o/p   - K.D.Patel

# 2. Find NUmber of spaces characters in a given str.
# input - Python Programming

# o/p - vowels - 4, white spaces - 1, consonents - 13

# 3. write a py program to make a new string
# input  - This is the lion in the cage.
# o/ p - This is lion in cage.

# 4. WAP:
# input - Keep yourself Mute while not speaking
# output - Keep_yourself Mute while not#speaking

# 5. Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 3 + 33 + 333 + 3333 + 33333 = ???

# 6. Write a Python function that checks whether a passed string is palindrome or not.

# 7. Write a Py program to calculate the factorial of a number (a non-negative integer).

# 8. Python program to find second largest number in a list.  // Null
