def royal(num1, num2=0):
    print(num1 + num2)

royal(10,20)   # 30
# royal(10)   # Error 

royal(20,111)
royal(20)

# Args --------

def Nilay(p,q,*kalaria,w=88):
    print(kalaria)   # (10, 20, 30, 'Techn', 90.23)

    for i in kalaria:
        print(i)


Nilay(10,20,30,"Techn", 90.23)


# kwargs ---------------

def Table(**kwargs):
    # return (kwargs)

    # for i in kwargs:
    #     print(i)
    for l,i in kwargs.items():
        print(l,i)


Table(name="Krutarth", roll = 900, address = "Ahm")   # {'name': 'Krutarth', 'roll': 900, 'address': 'Ahm'}


# def print1(num):
#     for i in range(num):
#         yield i

# user_need = int(input("ENter Number: "))
# for i in print1(user_need):
#     print(i)


list1 = [10,20,30,40,50]
list2 = [90,23,45,12,78]

ans = [(i,j) for i,j in zip(list1,list2)]
print(ans)   # [(10, 90), (20, 23), (30, 45), (40, 12), (50, 78)]

list2 = [10,23,42,51]
odd = []
for i in list2:
    if i % 2 != 0:
        odd.append(i)

print(odd)   # [23, 51]


# List Comprehension
odd1 = [i for i in list2 if i % 2 != 0]
print(odd1)


tup1 = (10,20,30,40,33,22,11)
combinations = []
for i in tup1:
    for j in tup1:
        combinations.append((i,j))

print(combinations)

# [(10, 10), (10, 20), (10, 30), (10, 40), (10, 33), (10, 22), (10, 11), (20, 10), (20, 20), (20, 30), (20, 40), (20, 33), (20, 22), (20, 11), (30, 10), (30, 20), (30, 30), (30, 40), (30, 33), (30, 22), (30, 11), (40, 10), (40, 20), (40, 30), (40, 40), (40, 33), (40, 22), (40, 11), (33, 10), (33, 20), (33, 30), (33, 40), (33, 33), (33, 22), (33, 11), (22, 10), (22, 20), (22, 30), (22, 40), (22, 33), (22, 22), (22, 11), (11, 10), (11, 20), (11, 30), (11, 40), (11, 33), (11, 22), (11, 11)]

res1 = [(i,j) for i in tup1 for j in tup1]
print(res1)


# [(2,8), (5,125) .....]

cube = [(i,i**3) for i in tup1]
print(cube)  # [(10, 1000), (20, 8000), (30, 27000), (40, 64000), (33, 35937), (22, 10648), (11, 1331)]