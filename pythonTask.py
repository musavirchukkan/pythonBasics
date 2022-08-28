# ############## task 1 #################

# 1
# Python program to print "Hello World"
print("Hello World")

# 2
# Python program to do sum of 'n' numbers, after taking inputs from the user
n = int(input("number of item to add : "))
list = []
sum = 0
for i in range(n):
    element = int(input("enter the item : "))
    list.append(element)
    sum = sum+element
print("entered elements are : ", list)
print("sum of entered elements is : ", sum)

#  3
# Write a python program to find the area of a square and rectangle.
while True:
    print("""
    1.Square
    2.circle
    3.rectangle
    4.triangle""")
    type = input("choose your option : ")
    if type == "1":
        length = int(input("enter the length of square : "))
        area = length*length
        print("area of square is : ", area)
    elif type == "2":
        radius = int(input("enter the radius of circle : "))
        area = 3.14*radius*radius
        print("area of circle is : ", area)
    elif type == "3":
        length = int(input("enter the length of rectangle : "))
        breadth = int(input("enter the breadth of rectangle : "))
        area = length*breadth
        print("area of rectangle is : ", area)
    elif type == "4":
        base = int(input("enter the base of triangle : "))
        height = int(input("enter the height of triangle : "))
        area = 0.5*base*height
        print("area of triangle is : ", area)
    else:
        print("invalid option")
    choise = input("do you want to continue (y/n) : ")
    if choise == "n":
        break

# 4
# Create a string & get the characters of string from 2 to 18 using both positive and negative indexing.
string = input("enter string : ")
print("positive indexing : ", string[1:17])
length = len(string)
print("negative indexing : ", string[-length+1:-length+17])

# 5
# Create and print a list with same and different items.
slist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("same items : ", slist)
dlist = [1, 2, "apple", 3.4, "cherry", {
    "kiwi", 5, "melon", 6}, (7, 8, "banana", 9)]
print("\n")
print("different items : ", dlist, "\n")

# 6
# Access an item from the list using its index.
list = ['apple', 2, 'banana', 30, 34, 'cherry', 55.65, 'orange', 45]
print("list : ", list)
indx = int(input("index of item : "))
print(list[indx])

# 7
# Access an item from the list using negative index.
list = ['apple', 2, 'banana', 30, 34, 'cherry', 55.65, 'orange', 45]
print("list : ", list)
length = len(list)
indx = int(input("index of item : "))
print(list[-length+indx-1])

# 8
# Modify an item in the list.
list = ['python', 'java', 'php', 'html', 'css', 'javascript']
print("list : ", list)
list.append("c++")
print("list appended : ", list)
list.insert(2, "c#")
print("list inserted : ", list)
list.remove("java")
print("list removed : ", list)

# 9
# Access the items in the list using slicing.
list = ['python', 'java', 'php', 'html', 'css', 'javascript']
print("sliced list : ", list[1:3])

# 10
# Create a dictionary and print it.
dict = {'name': 'musavir', 'age': '20', 'language': 'python', 4: 'index'}
print("dict : ", dict)

# 11
# Change the value of a key.
dict = {'name': 'musavir', 'age': '20', 'language': 'python', 4: 'index'}
print("dict : ", dict)
dict['age'] = '23'
print("changed dictionary : ", dict)


# ############## task 2 #################


# 1
# Create a string & demonstrate the functions

# capitalize()
sentence = "i love PYTHON"
capitalized_string = sentence.capitalize()
print(capitalized_string)
# casefold()
text = "pYtHon"
lowercased_string = text.casefold()
print(lowercased_string)
# center()
sentence = "Python is awesome"
new_string = sentence.center(25, '*')
print(new_string)
# count()
sentence = "python is awesome"
count = sentence.count('a')
print(count)
# encode()
sentence = "python is awesome"
encoded_string = sentence.encode()
print(encoded_string)
# endswith()
sentence = "python is awesome"
if sentence.endswith("awesome"):
    print("sentence ends with awesome")
else:
    print("sentence does not end with awesome")
# expandtabs()
sentence = "python\tis\ta\tawesome\tprogramming\tlanguage"
new_string = sentence.expandtabs(10)
print(new_string)
# find()
sentence = "python is awesome"
index = sentence.find('is')
print(index)
# format()
sentence = "python is awesome"
new_string = sentence.format()
print(new_string)
# format_map()
sentence = "python is awesome"
new_string = sentence.format_map({"python": "python"})
print(new_string)
# index()
sentence = "python is awesome"
index = sentence.index('is')
print(index)
# isalnum()
sentence = "python is awesome"
if sentence.isalnum():
    print("sentence is alphanumeric")
else:
    print("sentence is not alphanumeric")
# isalpha()
sentence = "python is awesome"
if sentence.isalpha():
    print("sentence is alphabetic")
else:
    print("sentence is not alphabetic")
# isdecimal()
sentence = "python is awesome"
if sentence.isdecimal():
    print("sentence is decimal")
else:
    print("sentence is not decimal")
# isdigit()
sentence = "python is awesome"
if sentence.isdigit():
    print("sentence is digit")
else:
    print("sentence is not digit")
# isidentifier()
sentence = "python is awesome"
if sentence.isidentifier():
    print("sentence is identifier")
else:
    print("sentence is not identifier")
# islower()
sentence = "python is awesome"
if sentence.islower():
    print("sentence is lowercase")
else:
    print("sentence is not lowercase")
# isnumeric()
sentence = "python is awesome"
if sentence.isnumeric():
    print("sentence is numeric")
else:
    print("sentence is not numeric")
# isprintable()
sentence = "python is awesome"
if sentence.isprintable():
    print("sentence is printable")
else:
    print("sentence is not printable")
# isspace()
sentence = "python is awesome"
if sentence.isspace():
    print("sentence is space")
else:
    print("sentence is not space")
# istitle()
sentence = "python is awesome"
if sentence.istitle():
    print("sentence is title")
else:
    print("sentence is not title")
# isupper()
sentence = "python is awesome"
if sentence.isupper():
    print("sentence is uppercase")
else:
    print("sentence is not uppercase")
# join()
sentence = "python is awesome"
new_string = sentence.join(["python", "is", "awesome"])
print(new_string)
# lower()
sentence = "python is awesome"
new_string = sentence.lower()
print(new_string)
# maketrans()
sentence = "python is awesome"
new_string = sentence.maketrans({"a": "b", "e": "f"})
print(new_string)
# partition()
sentence = "python is awesome"
new_string = sentence.partition("is")
print(new_string)
# replace()
sentence = "python is awesome"
new_string = sentence.replace("is", "is not")
print(new_string)
# split()
sentence = "python is awesome"
new_string = sentence.split(" ")
print(new_string)
# splitlines()
sentence = "python is awesome"
new_string = sentence.splitlines()
print(new_string)
# startswith()
sentence = "python is awesome"
if sentence.startswith("python"):
    print("sentence starts with python")
else:
    print("sentence does not start with python")
# strip()
sentence = "python is awesome"
new_string = sentence.strip()
print(new_string)
# swapcase()
sentence = "python is awesome"
new_string = sentence.swapcase()
print(new_string)
# title()
sentence = "python is awesome"
new_string = sentence.title()
print(new_string)
# translate()
sentence = "python is awesome"
new_string = sentence.translate({"a": "b", "e": "f"})
print(new_string)
# upper()
sentence = "python is awesome"
new_string = sentence.upper()
print(new_string)
# zfill()
sentence = "python is awesome"
new_string = sentence.zfill(25)
print(new_string)

# 2
