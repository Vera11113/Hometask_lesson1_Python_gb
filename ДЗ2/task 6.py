#структура данных Товары - список кортежей
#сделать аналитику о товарах

goods = []
features = {'название': '', 'цена': '', 'количество': '','единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [],'единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter":' ).upper() == 'Q':
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        pro = input(f'Введите значение свойства "{f}": ')
        f_copy[f] = int(pro) if f in 'цена количество' and pro.isdigit() else pro
        analitics[f].append(f_copy[f])
    goods.append((num, f_copy))
print(f"\nСтруктура товаров\n {goods}")
for key, v in analitics.items():
    print(f"{key}:{v}")
