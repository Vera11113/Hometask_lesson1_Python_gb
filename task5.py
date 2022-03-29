revenue = int (input('Введите выручку компании:'))
costs = int(input('Введите издержки компании:'))
if revenue > costs:
    print('Компания получила прибыль')
elif revenue == costs:
    print('Компания ничего не приобрела и не ушла в убыток')
else:
    print('У компании убыток')
