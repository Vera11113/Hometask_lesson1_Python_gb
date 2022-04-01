def my_func (x, y):
    num = 1
    for i in range(abs(y)) :
        num = num/x
    print(f'Значение {x} в степени {y} равно "{num:.4f}"')
    return

my_func(int(input('Введите число: ')),int(input('Введите степень числа (отрицательное число: ')))
