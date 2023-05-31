# python, code runner
# printf("ENter Your Name: ");
# scanf("%d",&h);

# name = input()  # Take input from user
# print(name)
# print("Welcome",name)   # Welcome Vidhi

# Python -> Dynamic Programming

# int x;
# float y;

x = 90
print(x)
print(type(x))  # <class 'int'>

y = 89.78
print(type(y))  # <class 'float'>

x = 78.0
print(type(x))  # <class 'float'>

g = "D"
print(type(g))  # <class 'str'>

e = '345'
print(type(e))  # <class 'str'>

w = "Yashvi"
print(type(w))

z = w   # Deep copy
print(type(z))  # <class 'str'>

z = 90
print(type(w))  # str

u = True
print(type(u))   # <class 'bool'>

q = 4+8j   # -> 4 is real part and 8j i simaginary part
print(type(q))  # <class 'complex'>

i = 8j
print(q+i)  # (4+98j)


g = None
print(type(g))  # <class 'NoneType'>

s = 90
e = 70
print(s+e)

# --------------------------

# Typecasting (TO convert one datatype to another datatype)

num1 = int(float(input("Enter first Number: ")))
num2 = int(input("Enter Second Number: "))
print("Sum of num1 and num2 is",num1+num2)   # Sum of num1 and num2 is 40.0


print("Sum of",num1,"and",num2,"is",num1+num2)
print(f"Sum of {num1} and {num2} is {num1 + num2}")  # fstring
print(f"Sum of {num1} and {num2} is {num1 - num2}")  # fstring
print(f"Sum of {num1} and {num2} is {num1 * num2}")  # fstring
print(f"Sum of {num1} and {num2} is {num1 / num2}")  # fstring   # 10.5  (returns float)
print(f"Sum of {num1} and {num2} is {num1 // num2}")  # fstring   # 10  (floor division return int value)
print(f"Sum of {num1} and {num2} is {num1 % num2}")  # fstring