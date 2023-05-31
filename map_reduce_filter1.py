# list1 = [10,20,30,40,50]

# square = lambda x : x**3
# print(square(40))   # 64000

# ans = []
# for j in list1:
#     ans.append(j*j)
# print(ans)  # [100, 400, 900, 1600, 2500]

# # Powerful FUnctions ---> Map, reduce, filter, eval, enumerate, zip

# cube = list(map(lambda x : x**3, list1))
# print(cube)   # [1000, 8000, 27000, 64000, 125000]

# str1 = ['11', '45', '90', '392']

# convert = tuple(map(lambda x : int(x),str1))
# convert = tuple(map(float,str1))   # (11.0, 45.0, 90.0, 392.0)

# # print(convert('45'))
# print(convert)

# x = list(map(int,[i for i in input().split()]))
# print(x)   # [30, 90, 21, 1, 1, 1, 1, 1, 3, 4]

# Filter -------------
list1 = [76,29,90,30,4]
gre_20 = list(filter(lambda x : x > 20, list1))

import statistics
gre_mean = list(filter(lambda x : statistics.mean(list1) < x, list1))
gre_mean = list(filter(lambda x : (sum(list1) // len(list1))  < x, list1))

print(gre_mean)   # [76, 90]

# (mean == Avg)

# median H.W


# Reduce -----------------------


list1 = [76,29,90,30,4]


from functools import reduce

add = reduce(lambda x,y : x+y,list1)
print(add)   # 229

from itertools import accumulate

add_1 = list(accumulate(list1,lambda x,y : x+y))
print(add_1)

num = 6
factorial = reduce(lambda x,y : x*y, [i for i in range(1,num+1)])
print(factorial)  # 720

# Map, reduce, filter ---> 5 Programs