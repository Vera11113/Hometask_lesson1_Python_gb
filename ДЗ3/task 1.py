#Позиционные аргументы

def division_f (del_1, del_2):
    """ Возвращает частное от деления.

     Позиционные аргументы:
     del_1 -- делимое
     del_2 -- делитель

    """
    try:
        div_f = del_1 / del_2
        print(f"Значение деления: {div_f:.2f}")
    except ZeroDivisionError as Error:
        print('Деление на 0, введите новые данные')
    pass

print("Программа будет выполнять деление. Введите 2 числа:\n")
division_f(int(input('Введите делимое: ')), int(input('Введите делитель: ')))