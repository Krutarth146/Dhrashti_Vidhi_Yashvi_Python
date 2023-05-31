list1 = [10,20,30,40,60]

ans = (map(lambda x : x**3, list1))  # <map object at 0x0000021E186B2F50>
ans = list(map(lambda x : x**3, list1))  # <map object at 0x0000021E186B2F50>
print(ans)  # [1000, 8000, 27000, 64000, 216000]


# filter
import statistics
avg = statistics.mean(list1)
print(list(filter(lambda x:x>avg, list1)))  # [40, 60]


# reduce 

from functools import reduce


list1 = [10,20,30,40,60]
print(reduce(lambda x,y : x+y, list1))  # 160
print(reduce(lambda x,y : x*y, list1))  # 14400000


from itertools import accumulate

print(list(accumulate(list1, lambda x,y : x*y)))  # [10, 200, 6000, 240000, 14400000]
print(list(accumulate(list1, lambda x,y : x+y)))  # [10, 30, 60, 100, 160]


# List Comprehension

list1 = [10,20,30,40,50, 10, 10,10]

# res = list1.copy()
# temp = [i for i in list1 if i not in res]

# print(temp)


temp = []

for i in list1:
    if i not in temp:
        temp.append(i)

print(temp)  # [10, 20, 30, 40, 50]



list2 = [20,30,40,51,60]

# Combinations

for i in list2:
    for t in list2:
        print(i,t)

list5 = [(i,t) for i in list2 for t in list2 if t%2!=0]
print(list5)  # [(20, 20), (20, 30), (20, 40), (20, 50), (20, 60), (30, 20), (30, 30), (30, 40), (30, 50), (30, 60), (40, 20), (40, 30), (40, 40), (40, 50), (40, 60), (50, 20), (50, 30), (50, 40), (50, 50), (50, 60), (60, 20), (60, 30), (60, 40), (60, 50), (60, 60)]


# lst9 = [10,77,44,223,801]

lst6 = [
    [10,20,30],
    [40,50,60],
    [30,21,24]
]


freq = int(input("Enter frequency: "))

# main = []

# for i in range(freq):
#     temp = []
#     for j in range(freq):
#         temp.append(int(input()))
#     main.append(temp)

# print(main)


main1 = []

for i in range(freq):
    x = [int(k) for k in input().split()]
    main1.append(x)

print(main1)


# Map, reduce, filter, list comprehension, Tuple Compre.  ---> 5 Programs of Each