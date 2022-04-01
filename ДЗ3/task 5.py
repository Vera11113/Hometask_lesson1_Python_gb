def sum_func(import_string):

    a = 0
    import_list = import_string.split()
    for i, item in enumerate(import_list):
       try:
            import_list[i] = int(item)
            a += int(item)
       except (ValueError or TypeError) as Error:
            import_list.pop(i)
            return [None, a]

    return [True, a]


whole_sum = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter"') == 'Q':
        break
    new_string = input('Введите набор чисел: ')
    new_list = sum_func(new_string)
    if True in new_list:
        whole_sum += new_list[1]
        print(f'Сумма чисел: {whole_sum}')
    else:
        whole_sum += new_list[1]
        print(whole_sum)
        print('Был введен символ, программа прекращает работу')
        break




