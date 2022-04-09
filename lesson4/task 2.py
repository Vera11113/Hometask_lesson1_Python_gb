my_list = [2, 12, 3, 5, 120, 3, 33, 45, 40, 99]
new_list = [v for i, v in enumerate(my_list) if (my_list[i] > my_list[i-1]) and (i != 0)]
print(new_list)