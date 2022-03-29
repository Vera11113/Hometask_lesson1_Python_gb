#Создать список и заполнить его элементами различных типов
#Вывести типы элементов

my_list = [1, 1.3, 'smth', True, [1, 2], None, {'a','b'}, {1: 'one'}]
print(my_list)

for i in my_list:
    print(i, type(i))
