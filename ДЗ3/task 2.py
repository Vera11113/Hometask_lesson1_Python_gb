def list_create (new_list, pro):
    new_list.append(pro)
    return new_list

my_list= []
data = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
for i in data:
    value = input(f'Введите значение "{i}": ')
    my_list = list_create(new_list=my_list, pro=value)

print(f"Данные о пользователе:\n {my_list}")

