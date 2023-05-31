# days = int(input())

# year = days // 365
# months = (days % 365) // 30
# remaining_days = (days % 365) % 30

# # print(year, months, remaining_days)

# print(f"Total Year is {year}, total months: {months}, reamining days are {remaining_days}")


r = True   # -> 1

print(type(r))
g = 90
print(type(g))   # Implicit TYpecasting


# Implicit TYpecasting and Explicit typecasting
h = int(r)  # Explicit typecasting
print(h)

print(r+g)  # 91


x = "90.45"

print(int(float(x)))  # 90.45

f = 80.98
print(int(f))   # 80

w = 'A'
# print(int(w))   # Gives Error

print(ord(w))   # 65


print(chr(89))   # Y



# Operators ---------------------------

# 1. Arithmetic    +     -    *      /(float)    //(floor)    % 

a = 90
b = 43
print(a+b)  # 179

print(a/b)   # 2.093
print(a//b)   # 2
print(a%b)    # 4


# Opearator Precedence and associativity

# 2. Assignment Operator  = += -= *= /= //= %= <<= >>= &= |= 

a = 90
a += 1   # a = a + 1  (Low Priority)
print(a)  # 91

a %=2   # 1
a -=8   # -7
print(a)   # -7


# 3. Comparison Operator  < > <= >=      == != <>
if a != b:
    print(True)

# 4. Logical Operator   -> and  or  not

a = 90
b = 78

# if()
# {


# }
# else{

# }

if a < b:
    print("90 is Max")
else:
    print("78 is Max")


# AND Table (a*b)
# 0 0 0
# 0 1 0
# 1 0 0 
# 1 1 1

# OR table (a+b)
# 0 0 0 
# 0 1 1
# 1 0 1
# 1 1 1 


# XOR table
# 0 0 0
# 1 1 0
# 0 1 1
# 1 0 1 

x = 90
y = 78
z = 56

if x > y and (x < z or y> z):
    print("If block is Executed")
else:
    print("ELse Executed")

    
