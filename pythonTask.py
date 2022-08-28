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
