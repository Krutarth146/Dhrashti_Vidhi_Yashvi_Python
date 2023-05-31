# for(i=1;i<=100;i+=1)
# {
#     //
# }


# for k in range(strat , end, step):
    # statements


for k in range(10):
    print(k,end=' ')   # start - 0 , End - 9 (n-1)  # 0 1 2 3 4 5 6 7 8 9

for j in range(3,25):  # start - 3, End - 24
    print(j,end=' ')
print()
for j in range(3,25,1):  # start - 3, End - 24, step - 0 (n-1)
    print(j,end=' ')  # 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24

print()
for j in range(3,25,3):  # start - 3, End - 24, step - 2 (n-1)
    print(j,end=' ')  # 3 6 9 12 15 18 21 24

print()
for j in range(35,25,3):  # null
    print(j,end=' ')  # 

print()
for j in range(35,25,-1):  # start - 35, End - 26, step - 0 (n-1)
    print(j,end=' ')  # 35 34 33 32 31 30 29 28 27 26

print()
for j in range(35,2,-3):  # start - 35, End - 3, step - 2 (n-1)
    print(j,end=' ')  # 35 32 29 26 23 20 17 14 11 8 5

print()
for j in range(-10,-2,-3):  # start - 35, End - 3, step - 2 (n-1)
    print(j,end=' ')  # null

print()
for j in range(-10,-20,-3):  # start - -10, End - -19, step - 2 (n-1)
    print(j,end=' ')  # -10 -13 -16 -19


list1 = [10, 90, 89, 67, 56]

for i in list1:
    print(i)

for j in range(len(list1)):
    print(list1[j],end=' ')  # list1[0], list1[1]..... # 10 90 89 67 56


