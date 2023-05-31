list1 = [90,78,67,56,33,220, 90.89, True, [2,3,4], (43,4,5), 3+9j, "Vidhi", 'Y', 'Y']
print(list1)  # [90, 78, 67, 56, 33, 220]

print(type(list1))  # <class 'list'>

print(list1.__sizeof__())  # 144

print(id(list1))  # 2492683465408

list2 = list1   # -------------- # Deep copy

list3 = list1.copy()  # --------------  # Shallow copy

list1.append(800)

print(list2)  # [90, 78, 67, 56, 33, 220, 90.89, True, [2, 3, 4], (43, 4, 5), (3+9j), 'Vidhi', 'Y', 800]
print(list3)  # [90, 78, 67, 56, 33, 220, 90.89, True, [2, 3, 4], (43, 4, 5), (3+9j), 'Vidhi', 'Y']

print(id(list1))  # 2289020646080
print(id(list2))  # 2289020646080
print(id(list3))  # 2289020649024

print(len(list1))   # 15
print(list1)  # Allows Duplicates, Ordered (Indexed), Mutable (Changeble)

list1.append("String")

print(list1)  # [90, 78, 67, 56, 33, 220, 90.89, True, [2, 3, 4], (43, 4, 5), (3+9j), 'Vidhi', 'Y', 'Y', 800, 'String']


# list1.clear()
# print(list1)   # []


print(list1.count('Y'))   # 2

list1 = [12, 90, 78, 67, 45, 45, 33, 12]
print(len(list1))     # 8 -> Index starts from 0, Length starts from 1


list1.append(100)
print(list1)  # [12, 90, 78, 67, 45, 45, 33, 12, 100]

list1.append("Dhr")
print(list1)
print(list1) # [12, 90, 78, 67, 45, 45, 33, 12, 100, 'Dhr']
list1.insert(3,"Aman")
print(list1)
# list1.insert(-1,"Aman")
# print(list1)


# list1.extend(100)   # Int object is not Supported
# list1.extend('100')   # Int object is not Supported
# list1.extend('Vidhi')   # Int object is not Supported
# print(list1)

list2 = [10,20,30,40]

# list1.append(list2)
# print(list1)   # [12, 90, 78, 'Aman', 67, 45, 45, 33, 12, 100, 'Dhr', [10, 20, 30, 40]]

# list1.extend(list2)
# print(list1)  # [12, 90, 78, 'Aman', 67, 45, 45, 33, 12, 100, 'Dhr', 10, 20, 30, 40]

list1.pop()
print(list1)  # [12, 90, 78, 'Aman', 67, 45, 45, 33, 12, 100]

list1.pop(3)
print(list1)  # removes PArticular index element

# list1.remove(12)

# print(list1)

# num = int(input())
# for _ in list1:
#     if _ == num:
#         list1.remove(_)
# print(list1)

# list4 = list1.copy()  # shallow copy

# list5 = list1    # deep copy

# list1.append(900)

# print(list4)  # [12, 90, 78, 67, 45, 45, 33, 12, 100]
# print(list5)  # [12, 90, 78, 67, 45, 45, 33, 12, 100, 900]

print(list1.index(33))   # 6

# list1.reverse()
# print(list1)  # [100, 12, 33, 45, 45, 67, 78, 90, 12]

# list1.sort(reverse=False)
# print(list1)  # [12, 12, 33, 45, 45, 67, 78, 90, 100]
# list1.sort(reverse=True)
# print(list1)  # [100, 90, 78, 67, 45, 45, 33, 12, 12]

print(sum(list1))   # 482
print(sum(list1) // len(list1))   # 53
print(min(list1))   # 12
print(max(list1))   # 100

for j in sorted(list1):
    print(j)

print(list1[3])  # 67
# List: ordered (Indexed), Allow Duplicates, Mutable (Changeble)


list1 = set(list1)
print(list1)  # {33, 67, 100, 12, 45, 78, 90}



# Task-:
# 1. Create a list of Fruits(15 exotic fruits)
# take user input and check if the fruits are avail in the list
# if available print "fruit_name is Available"


# 2. create a list of numbers(15 numbers (1-100))
# sort that list in ascending order
# search for the number in the list
# take input from user and find all the occurence
# print the occurence


# Tasks-: 
#     1. Wap to find no. of month from the given no. of days
#     2. wap to scan seconds and print hour, minute and remaining seconds
#     3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
#     4. wap to check whether the number is odd or even
#     5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
#     6. wap to make any user inputted string in uppercase or lowercase
#     7. wap to print the sum of user entered numbers (scan by the user)
#     8. wap to find power of a number
#     9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
#     Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
#     eg: base = 2, power=10
#     output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    # list programs
    # 1. add 5 numbers into the list and print the list
    # 2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    # 3. add 10 numbers into the list, sort that list and print the list
    # 4. add 10 numbers into the list, remove the duplicates and print the list
    # 5. add 10 numbers into the list, print the maximum and minimum number from the list
    # 6. add 10 numbers into the list, print the average of the list
    # 7. add 10 numbers into the list, print the sum of the list
    # 8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    # 9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    # 10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    # 11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    # 12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.



# list1 = [1,2,3,4,5,6]
# print(list1)

# # list1 = [[1,2,3], [4,5,6], [7,8,9]]

# num = int(input())
# list1 = []

# for i in range(num):
#     list2 = [int(i) for i in input().split()]
#     list1.append(list2)
# print(list1)

# for i in range(len(list1)):  # 0
#     if i % 2 == 0:
#         for j in range(len(list1[0])):  # 
#             print(list1[i][j],end = ' ')  # 1 0
            
#     elif i % 2 !=0 :
#         # j = 2
#         # while j>=0:  # 
#         #     print(list1[i][j],end=' ')  # 1 0 
#         #     j-=1

#         for j in range(len(list1[0])-1,-1,-1):
#             print(list1[i][j],end=' ')

base = 2
power = 8
list1 = []
mul = 1
for i in range(power):
    mul *= base

    print(mul,end=' ')
    list1.append(mul)

print(list1)

matrix = [[22,5,8],[3,5,4],[9,5,7]]
len1 = len(matrix)
diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][len1-1-i]
print("sum of diagonal matrix elements : ", diagonal_sum)