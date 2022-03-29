revenue = int(input('Введите выручку компании:'))
costs = int(input('Введите издержки компании:'))
if revenue > costs:
    print('Компания получила прибыль')
    income = revenue - costs
    rent = (income/revenue)*100
    print(f'Рентабельность фирмы составляет - {rent:.2f}%')
    workers = int(input("Введите количество сотрудников"))
    income_worker = income / workers
    print(f'Прибыль компании в расчете на 1 сотрудника составляет {income_worker:.2f} руб')
elif revenue == costs:
    print('Компания ничего не приобрела и не ушла в убыток')
else:
    print('У компании убыток')