

def fact(k):
    f_num = 1
    for i in range(k+1):
        yield (f'{i}! = {f_num}')
    f_num *= i + 1

n = int(input('Введите n: '))
for el in fact(n):
    print(el)
    