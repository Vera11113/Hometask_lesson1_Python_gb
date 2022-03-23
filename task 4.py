number = int(input("введите число:"))
max = 0
lonely_number = number % 10
number = number // 10
while number // 10 != 0:
    if lonely_number > max:
        max = lonely_number
    lonely_number = number % 10
    number = number // 10
print(f'Максимальная цифра числа = {max}')
