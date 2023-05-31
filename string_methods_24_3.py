str3 = "lor.em\tipsum. 123."

print(len(str3))   # 16
print(str3.center(20,'*'))  # **lorem ipsum 123.**
print(str3.count('.'))   # 3

print(str3.encode())  # b'lor.em ipsum. 123.'

str5 = "Såtåle"
print(str5.encode())  # b'St\xc3\xa5le'

print(str5.encode(encoding="utf-8",errors="replace"))  # b'St?le'
print(str5.encode(encoding="ASCII",errors="ignore"))  # b'Stle'
print(str5.encode(encoding="ASCII",errors="backslashreplace"))  # b'St\\xe5le'
print(str5.encode(encoding="ASCII",errors="xmlcharrefreplace"))  # b'St&#229;le'
print(str5.encode(encoding="ASCII",errors="namereplace"))  # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'

print(str3.endswith('3'))   # False
print(str3.expandtabs(16))   # lor.em          ipsum. 123.

str3 = "lor.em\tipsum. 123."
# print(str3.find('e'))   # 4
# print(str3.index('e'))  # 4

print(str3.find('z'))   # -1  # Returns -1 if element is not Found
# print(str3.index('z'))  # 4   Generates Error if element is Not Found


str4 = "{name} is Good {gender}.".format(name="Aman", gender= "Male")
print(str4)  # Aman is Good Male.

str4 = "{} is Good {}.".format("Aman", "Male")
print(str4)  # Aman is Good Male.


str4 = "{1} is Good {2}. {0}".format("Dubai", "Aman", "Male")
print(str4)  # Aman is Good Male. Dubai

dict1 = {"Name" : "Vidhi", 'ROll' : 90}
print(dict1)  # {'Name': 'Vidhi', 'Roll': 90}


str4 = "{Name}'s ROll nimber is {ROll}"
print(str4.format_map(dict1))   # Vidhi's ROll nimber is 90


x = 90
y = 80
print(f"{x} + {y} = {x+y}")   # 90 + 80 = 170

str3 = "Loremipsum123"
print(str3.isalnum())   # True
print(str3.isalpha())   # False

print(str3.isnumeric())   # False
print(str3.isdigit())   # False
print(str3.isdecimal())   # False

print(str3.isidentifier())   # True
print(str3.isprintable())     # True
print(str3.isascii())   # True
print(str3.isspace())   # False
print(str3.istitle())   # True