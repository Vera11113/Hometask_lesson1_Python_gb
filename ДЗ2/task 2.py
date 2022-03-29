new_list = input('Введите список: ')
print(new_list)
my_list = list(new_list.split())

for i in range(len(my_list)-1):
    if i % 2 == 0:
        a = my_list[i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = a

print(my_list)



