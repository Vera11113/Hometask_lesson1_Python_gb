from sys import argv

num, hours, price, bonus = argv
print(argv)
print(f'Количество часов: {hours}')
print(f'Ставка в час: {price}')
print(f'Бонусы: {bonus}')
print('Заработная плата составляет: ', int(hours)*int(price)+int(bonus), 'долларов США')
