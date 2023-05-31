set1 = {}
print(set1)
print(type(set1))   # <class 'dict'>

set2 = {10}
set3 = set()

print(type(set2), type(set3))   # <class 'set'> <class 'set'>

set3 = {10, 90.89, True, "str1", (10,20,30,40),10,10,10}
print(set3)  # {True, (10, 20, 30, 40), 90.89, 'str1', 10}

# Set ----> Don't Allow Duplicates, Unordered, Unchangeble (*but we can add or remove elements)


list1 = [10,10,10,20,340,10]
print(set(list1))   # {10, 20, 340}

set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(len(set1))   # 4
# print(set1[2])   # Unordered   Gives Error

print(sorted(set1))
set1.add("Manoj")
# set1.add([[10,20,30]])
set1.update([10,20,30, "str1"])
print(set1)

# set1.clear()

# del set1
print(set1)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.difference(set2))   # {10,20}
# set1.difference_update(set2)

# print(set1)  # {10,20}



set1.remove(20)   # Generates Error If ELement is Not FOund
print(set1)  # {40, 30}
set1.discard(20)  # Ignores if Element is Not Found
print(set1) # {40, 10, 30}

print(set1.intersection(set2))  # {40,30}

set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.issuperset(set2))   # True
print(set1.isdisjoint(set2))  # True
print(set2.issubset(set1))  # True

set1.pop()
set1.pop()
set1.pop()
print(set1)
set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.symmetric_difference(set2))  # {10, 50, 20, 60}
print(set1.difference(set2))   # {10, 20}


set1 = set1.union(set2)
print(set1)