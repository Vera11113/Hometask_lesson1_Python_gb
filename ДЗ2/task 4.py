new_string = input('Введите последовательность слов: ')
new_list = list(new_string.split())
#print(new_list)

for i in new_list:
    print(f"{i:.10}")


