list1 = [[10,90,89,78], [46,68,32,11], [88,44,22,43]]

# FInd Second Largest
ans = [89,46,44] 

for i in list1:
    print(sorted(i)[-2])

res = list(map(lambda x : sorted(x)[-2],list1))
print(res)  # [89,46,44]


# Vehicle = 200    2w + 4w
# wheels =  540

# 2w??   4w???


str1 = "Vi#d#h*i*"

vidhi = 0
dhr = 0

for i in str1:
    if i == '#':
        vidhi+=1
    elif i == '*':
        dhr+=1

if dhr == vidhi:
    print(1)
else:
    print("Fail")


# count of '#' and '*' is Same then print(1)

# MISSISSIPPI -----> {'M' : 1, 'I' : 4, 'S' : 4, 'P' : 2}

str1 = "MISSISSIPPI"
dict1 = {}
for i in str1:
    if i not in dict1:
        dict1[i] = 1
        # dict1["Roll"] = 8000  Concept
    else:
        dict1[i] += 1


print(dict1)


dict1 = {"Name" : "Krutarth", 'Roll' : 900}  # Mutable (Changeble), Ordered

# Key - value Pair

# Name, Roll ----> Keys (Unique)
# Krutarth, 900 -----> Value (Allow's Duplicates)

print(dict1.keys())  # dict_keys(['Name', 'Roll'])
print(dict1.values())  # dict_values(['Krutarth', 900])


print(dict1.get("Name"))   # Krutarth
print(dict1['Roll'])

dict1["Roll"] = 8000
print(dict1)  # {'Name': 'Krutarth', 'Roll': 8000}


# Next Topic --- File, Nested lambda, Exception Handling


'''
"""
Functions Examples:
1. Ask two integers from user, add their factroials. Now ask two more integers from user and add their factorials too. calculate average of the factorials you computed. Now finally ask one last integer from user and add its factorial to the average.
2. Write a function that prints whether the number passed in its argument is prime or not. Using a main program pass the number given by the user to that function.
3. Write a function to find average of 5 given numbers and a main program that takes 5 integers from user, uses the factorial function to find factorial of each one of them and using average function prints the average of factorials of them.
4. Make a program that uses a function to find nth term of an arithmetic progression whose first term is a & common difference is d.
    ap:
    first term = a = 5
    difference = d = 4
    ap = 5, 9, 13, 17, 21, 25,...
    nth term = a + (n-1)d
5. Develop a program that uses a function to find nth term of an geometric progression whose first term is 'a' & common ratio is 'r'.
formula: a * r^(n-1)
6. Make a function that checks whether the given number is a perfect number or not. Make a program that uses this function to print all the perfect numbers between a given range. A perfect number is one whose all factors (excluding itself), when added up, you get the number itself. eg, factors of 6: 1, 2, 3, 6 & 1+2+3 = 6. so 6 is a perfect number.
7. Write a function that determines whether the number given in its argument is a Prime number or not. Build a main program that takes two integers from user and print all the Prime numbers between those two integers using that function.
8. Write a function that determines whether the number given in its argument is Armstrong number or not. Build a main program that takes two integers from user and print all the Armstrong numbers between those two integers using that function.
9. Royal Kids Bank
Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""



# 1. Make a list containing of only strings. Now ask user for any string and re-arrange the list in the decending order of occurance of that string.

# for example:
# list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
# input string = 'bug'
# output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']



2. Create a Python program to generate user-defined set. Then ask user to eneter any value & check if the given value is present in a set or not.
3. Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
4. Use dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask user to enter a word and display antonym of it.
5. Ask user to give name and marks of 10 different students. Store them in dictionary.
6. Sort the above dictionary by the names of students.
7. Sort the dictionary in ex-5 by the marks.
8. Make a Python program to count letters of the word: MISSISSIPPI. Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user.
9. Write a Python program to split a given dictionary of lists into list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
"""
'''



# num = int(input())
# step = int(input())

# # 3 + 33 + 333 + 3333 + 33333 = ??
# temp = num
# sum = 0
# sum += num

# for i in range(step-1):
#     temp = temp * 10 + num
#     sum += temp
#     print(temp)

# print(sum)


# # Leap Year :
# for year in range(1990,3001):
#     if year % 400 == 0:
#         print(year,end=' ')
#     if year % 4 == 0 and year % 100 != 0:
#         print(year,end=' ')



# tup1 = (78,90, {"Name" : ["Drashti", "Vidhi", "Yashvi"]})

# print(tup1[-1]["Name"][2])
# print(tup1[-1]["Name"][-1])
# print(tup1[-1].get("Name")[-1])


matrix = [[10,20,30], 
          [90,89,78], 
          [57,67,32]]

print(len(matrix))   # 3

for i in matrix:
    print(i)


list1d = []

for i in range(len(matrix)): # 0 1 2             # i = 2
    for j in range(len(matrix[i])):  # 0 1 2     # j = 2
        print(matrix[i][j],end=' ')
    print()

# matrix.sort()
# print(matrix)

sorted_list = []
for k in matrix:
    k.sort()
    sorted_list.append(k)

sorted_list.sort()
print(sorted_list)