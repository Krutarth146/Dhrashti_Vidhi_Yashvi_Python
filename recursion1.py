# Recursion
# when function calls itself then it is called as Recursion

def fibonnacci(num):
    n1,n2 = 0,1
    i=0
    print(n1,n2,end=' ')

    while(i<num-2):
        n3 = n1 + n2
        print(n3,end=' ')
        n1 = n2
        n2 = n3
        i+=1

fibonnacci(5)
print()
print()
print()

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibo_recursion(num):
    if num==0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo_recursion(num-1) + fibo_recursion(num-2)
    
# print(fibo_recursion(6))   # 8

for i in range(5):
    print(fibo_recursion(i),end=' ')

# 1 to 100 Print using Recursion      ,,,,,,     Factorial Program




# Lambda (Anounomous Function)


list1 = [10,20,30,40,50,60]

def square(list90):
    temp = []
    for i in list90:
        temp.append(i**2)
    return temp

# print(list90)

print(square(list1))  # [100, 400, 900, 1600, 2500, 3600]


square_lam = lambda x : x*x

print(square_lam(26))

print(map(lambda x:x*x, list1))  # <map object at 0x000002509166FD30>
print(list(map(lambda x:x*x, list1)))  # [100, 400, 900, 1600, 2500, 3600]

# Powerful FUnctions ---> Map, reduce, filter
# lambda,zip, enumerate

list1 = [10,20,30,40,500]
list2 = [2,3,5,7,9]


res = [{i,j} for i,j in zip(list1,list2)]
print(res)  # [(10, 2), (20, 3), (30, 5), (40, 7), (500, 9)]


ans = [h for h in enumerate(list1,100)]
print(ans)  # [(100, 10), (101, 20), (102, 30), (103, 40), (104, 500)]


def quadratic_fun(a,b,c):
    return lambda x : (a*x**2 + b*x + c)


vidhi = quadratic_fun(10,20,30)

print(vidhi(5))   # 380


# Recursion, lambda 10 Programs