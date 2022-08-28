# ############## task 1 #################

# 1
print("Hello World")

# 2
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
string = input("enter string : ")
print("positive indexing : ", string[1:17])
length = len(string)
print("negative indexing : ", string[-length+1:-length+17])
