tup1 = (10,10,20,30,40.89,10,10,"Krutarth", True,(1,2,3),[2,3,4],{90,89,78})
list1 = [10,10,20,30,40.89,"Krutarth", True,(1,2,3),[2,3,4],{90,89,78}]
print(tup1)

print(tup1.__sizeof__())   # 104  # Storage Efficient
print(list1.__sizeof__())  # 120

# Tuple charcteristics: 

# Tuple - Allow Duplicates, ordered, Immutable (Not Changeble)


# Indexing
print(tup1[-2]) # [2,3,4]
print(tup1[5])  # 10

# Slicing
print(tup1[0:4])  # (10, 10, 20, 30)

print(tup1[5:8:1])   # start - 5, end = 7 (n-1), step - 0 (n-1)  # (10, 10, 'Krutarth')


tup1 = (10,10,20,30,40.89,10,10,"Krutarth", True,(1,2,3),[2,3,4],{90,89,78})
print(tup1[-2:-6:-3])  # [[2,3,4], "Krutarth"]

print(tup1[-4:3:2])  # ()


# Tuple Methods
tup1 = (10, 90, 90, 89, 78, 67)

print(tup1.count(90))   # 2
print(tup1.index(90))   # 1

# tup1[6] = 90
# print(tup1)  # Item assignment is not supported

tup1 = (10, 90, 90, 89, 78, 67)

for j in tup1:
    print(j)

# tup1 = tuple(set(tup1))
# print(tup1)  # {67, 10, 78, 89, 90}

# set1 = {10,10,10,10,10,10,10,10}

# print(set1)  # {10}  # Unique Values


for j in sorted(tup1):
    print(j)

print(tup1,end=' ')

list1 = list(tup1)

list1.append(100)
list1.append(200)
list1.append(300)
list1.append(400)

list1.remove(90)
list1.remove(90)


print()
print(list1)  # [10, 89, 78, 67, 100, 200, 300, 400]

tup1 = tuple(list1)
print(tup1)  # (10, 89, 78, 67, 100, 200, 300, 400)


list1 = [10,90,78,34,89]

list1.sort(reverse=False)
print(list1)