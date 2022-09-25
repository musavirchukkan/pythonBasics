digit = int(input("Enter a digit : "))
rev = 0
while digit > 0:
    rev = rev*10+digit % 10
    digit = digit//10
print("Reversed digit : ", rev)
