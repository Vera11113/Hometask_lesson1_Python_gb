my_list = [2, 1, 3, 4, 5, 21, 5, 23, 4, 2, 90]
new_list = [item for item in my_list if my_list.count(item) == 1]
print(new_list)