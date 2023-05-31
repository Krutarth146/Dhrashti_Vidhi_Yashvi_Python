list1 = [10, 90, 89, 78, 67]

# list1.append(90)
# print(list1)


# freq = int(input())   # 5
# for i in range(freq):  # 0 1 2 3 4
#     list1.append(int(input()))

# print(list1)

# Matrices

list1 = [[1,2,3], [4,5,6], [7,8,9]]

print(len(list1))   # 3  # starts from 1, Index starts from 0

# print(list1[0])  # [1,2,3]
# print(list1[-1])  # [7,8,9]
count = 0

# for i in list1:
#     print(i)  # [1,2,3]    [4, 5, 6]   [7, 8, 9]
#     count+=1

# print(count)  # 3

sum = 0

for j in list1:  # [1,2,3]
    for g in j:
        print(g,end=' ')  # 1 2 3 4 5 6 7 8 9
        sum += g
        count+=1
print()
print(sum//count)

# list1[i][j]


num = int(input())  # 5

power = int(input())  # 2

# print(num ** power)

i = 0
ans = 1
while i<power:
    ans *= num  # 125
    i+=1

print(ans)