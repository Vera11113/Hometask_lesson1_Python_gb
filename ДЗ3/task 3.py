def my_func(s1, s2, s3):
    sum_list = [int(s1), int(s2), int(s3)]
    sum_list.sort(reverse= True)
    max = sum_list[0] + sum_list[1]
    print(f'Максимальная сумма у чисел "{sum_list[0]}" и "{sum_list[1]}"\n')
    print(f'Сумма равна: "{max}" ')
    return



my_func(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: '))
