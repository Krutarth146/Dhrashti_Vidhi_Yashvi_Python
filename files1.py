'''
    FIles --> 1. Text FIle (t)    2. Binary FIle (b)

    # FIles OPening Modes

    'w' ---> Write Mode (Overwrite)

    'r' ---> Read Mode (FIle needed)

    'a' ---> Append Mode  (No Overwrite)

    'x' ---> If file Exists then It will Generate an Error

    '+' ---> Read + Write
'''
# FILE *fp;
fp = open("vidhi.txt","w")
fp.write("Hello Your Name is Dhrashti Kalaria")

list1 = ["\nRoyal Techno\n", "Gujarat T University\n" , "Silveroak University\n"]
fp.writelines(list1)
fp.close()

f1 = open("vidhi.txt","r")
print(f1.tell())  # 0
# x = f1.read()
print(f1.tell())  # 95

# lst = x.split()
# print(lst)
# print(x)
# counter = 0
# for j in f1.read():
#     print(j)
#     counter+=1

print(f1.readline())  # Hello Your Name is Dhrashti Kalaria
print(f1.tell())   # 37
print(f1.readline())  # Royal Techno
print(f1.tell())   # 51
print(f1.readline())  # Gujarat T University
print(f1.readline())  # Silveroak University

f1.seek(37)
print(f1.readline())      # Royal Techno

f1.seek(0)
print(f1.readlines())  # ['Hello Your Name is Dhrashti Kalaria\n', 'Royal Techno\n', 'Gujarat T University\n', 'Silveroak University\n']
f1.close()


# for h in lst:
#     if h.startswith("S"):
#         print("Starts with S")
#         print(h)

# print(counter)  # 89


# Total Words, Characters, starts with 'a'
# Prime Number print, amstrong Number print in particular File