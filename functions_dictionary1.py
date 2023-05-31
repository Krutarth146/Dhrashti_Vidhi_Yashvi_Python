# Function -> Code Reusability

# Func. Declaration -- No


#include<stdio.h>
# void swap();   // Func. Declaration



# main()
# {
#        swap();   // Func. Calling

# }


# void swap()   // Func. Defination
# {
#     int x, y, temp;
#     temp = x;
#     x = y;
#     y = temp;
# }
# ------------------------------------------
# 1. Func. Defination
# 2. Func. Calling

# 1. without return type and W/o args.
# 2. W/o return type and With args.
# 3. with return type and W/o args.
# 4. with return type and with args.

def Yashvi():
    print("Hello")

Yashvi()

# 1. without return type and W/o args.

def sum():
    print(95**2)

sum()   # 9025

# 2. W/o return type and With args.

def div(x, y, c=0, u=0):
    print(x//y-c+u)

div(20,3,90,800)   # 716

def joint(str1,str2,str3=None):
    print(str1+str2)
    print(str3)

joint("Kru", "tarth")  # Krutarth   None

# 3. with return type and W/o args.

def appenda():
    list1 = [10,20,30,40]
    return list1

print(appenda())  # [10, 20, 30, 40]


# 4. with return type and with args.

list1 = [(10,20,30),(40,50,61,67),(90,80,99)]

def odd(list555):
    ans = []
    for i in list555:
        for j in i:
            if j % 2 != 0:
                ans.append(j)

    return ans

x = odd(list1)
print(x)


def random1(x,y,*vidhi):
    print(type(vidhi))  # <class 'tuple'>
    print(vidhi)
    sum = 0
    for i in vidhi:
        sum += i
    return sum

print(random1(10,20,30,40,506,66,777,22))  # (10, 20, 30, 40, 506, 66, 777, 22)   # 1441


x = 80

def modify():
    # x = 78
    global x
    x+=10
    print(x)

# modify()   # 90
# print(x)   # 90


num1 = 80
num2 = 560
num3 = 6700

# Use Lambda

maximum = lambda num1,num2,num3 : (print(num1) if num1 > num3 else print(num3)) if num1 > num2 else (print(num2) if num2 > num3 else print(num3))
maximum(num1,num2,num3)  # 6700