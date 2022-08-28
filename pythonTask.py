# ############## task 1 #################

# 1
from multiprocessing.heap import Arena


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
print("""1.Square
2.circle
3.rectangle
4.triangle""")
type = input("choose your option : ")
