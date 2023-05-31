#include<stdio.h>

# import numpy

num1 = int(input("ENter first Number: "))
num2 = int(input("ENter second Number: "))
num3 = int(input("ENter Third Number: "))

# if num1 > num2:
#     if num1 > num3:
#         print(f"{num1} is Max.")
#     else:
#         print(f"{num3} is Max.")
# else:
#     if num2 > num3:
#         print(f"{num2} is Max")
#     else:
#         print(f"{num3} is Max.")

# # ( Condition ? Exp1 : Exp2)

var = (num1 if num1 > num2 else num2)
print(var)   # H.w  3 variables 



# while()

# Intialization ,condition, Flow


# int i = 0;
# while(i<=100)
# {
#     printf("%d",i);
#     i+=1;
# }

# _ = 0   # Intialization

# while _ <= 100:   # condition
#     print(_,end=' ')   # statement
#     _+=1   # Flow

# _ = 99   # Intialization

# while _ >= 1:   # condition
#     print(_,end=' ')   # statement
#     _-=4   # Flow

_ = 99   # Intialization

# while _ >= 1:   # condition
#     if _ % 5 == 0:
#         print(_,end=' ')   # statement   95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 
#     _-=1   # Flow


while _ >= 1:   # condition
    if _ % 5 == 0 and _%10 == 0 or (_%2 == 0 or _%7 == 0):
        print(_,end='\t')   # statement   95 90 85 80 75 70 65 60 55 50 45 40 35 30 25 20 15 10 5 
    _-=1   # Flow

# 98 96 94 92 91 90 88 86 84 82 80 78 77 76 74 72 70 68 66 64 63 62 60 58 56 54 52 50 49 48 46 44 42 40 38 36 35 34 32 30 28 26 24 22 21 20 18 16 14 12 10 8 7 6 4 2


# Hw -> Table, Prime, Palindrome,Armstrong, Perfect, Twin, COunt total divisors, Total Digits, Reverse Number
# Check age for voting, 
# print numbers divisible by 5 and 7 b/w 400 to 900.