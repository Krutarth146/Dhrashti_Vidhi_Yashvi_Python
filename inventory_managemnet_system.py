# Dictionary: key-value Pair  (key -> Unique), Mutable (Changeble), Ordered

dict1 = {}
print(type(dict1))   # <class 'dict'>

set1 = {}
print(type(set1))    # <class 'dict'>

set2 = {10}
print(type(set2))  # <class 'set'>

dict2 = {'Name' : "Ruturaj", 'mobile' : 992992929, 'roll' : 45, 'Address' : {'city' : "Gnr", 'state' : "Guj"}, 'Name' : "Manoj"}

print(dict2)   # {'Name': 'Ruturaj', 'mobile': 992992929, 'roll': 45, 'Address': {'city': 'Gnr', 'state': 'Guj'}}

print(dict2.keys())  # dict_keys(['Name', 'mobile', 'roll', 'Address'])
print(dict2.values())  # dict_values(['Ruturaj', 992992929, 45, {'city': 'Gnr', 'state': 'Guj'}])
print(dict2.items())  # dict_items([('Name', 'Ruturaj'), ('mobile', 992992929), ('roll', 45), ('Address', {'city': 'Gnr', 'state': 'Guj'})])

dict2.update({"college" : "LDRP", 'Institute' : "ROyal"}) 
print(dict2)   # {'Name': 'Manoj', 'mobile': 992992929, 'roll': 45, 'Address': {'city': 'Gnr', 'state': 'Guj'}, 'college': 'LDRP'}

print(dict2["Name"])  # Manoj
print(dict2.get("roll"))  # 45
print(dict2['Address']['state'])  # Guj


for i,j in dict2.items():
    print(i,j)

# dict2.clear()
# print(dict2)  # {}

del dict2["Address"]
print(dict2)  # {'Name': 'Manoj', 'mobile': 992992929, 'roll': 45, 'college': 'LDRP'}

list1 = ['str1', 'str2', 'str3']
val = 0
x = dict.fromkeys(list1,val)
print(x)   # {'str1': 0, 'str2': 0, 'str3': 0}

dict2['school'] = "HbK"
print(dict2)  # {'Name': 'Manoj', 'mobile': 992992929, 'roll': 45, 'college': 'LDRP', 'Institute': 'ROyal', 'school': 'HbK'}


c = dict2.pop('roll')
print(c)
print(dict2)  # {'Name': 'Manoj', 'mobile': 992992929, 'college': 'LDRP', 'Institute': 'ROyal', 'school': 'HbK'}

dict2.popitem()
print(dict2)  # {'Name': 'Manoj', 'mobile': 992992929, 'college': 'LDRP', 'Institute': 'ROyal'}


dict2.setdefault('std',9)
print(dict2)


# -----------------------------------------------

record = {'1001' : {'pName' : "5 star", 'qn' : 90, 'price' : 20},
          '1002' : {'pName' : 'Oats', 'qn' : 190, 'price' : 30}, 
          '1003' : {'pName' : 'Kellogs', 'qn' : 200, 'price' : 50},
          '1004' : {'pName' : 'Parle G', 'qn' : 400, 'price' : 5},}

print(record)
print(record['1003']['price'])  # 50
print(record['1002']['qn'])  # 50

user_need = input("Enter Product Id: ")
quantity = int(input("Enter QUantity: "))

total_bill = 0
if quantity <= record[user_need]['qn']:
    total_bill = quantity * record[user_need]['price']
    record[user_need]['qn'] -= quantity
    print("Your Bill Amount is",total_bill)
    print("Inventory Updated!!")
else:
    pass