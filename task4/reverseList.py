original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list: ", original_list)
reversed_list = []
for i in original_list:
    reversed_list = [i]+reversed_list
print("Reversed list: ", reversed_list)
