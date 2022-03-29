month_number = int(input('Введите номер месяца: '))
season = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8],
          'осень': [9, 10, 11]}

for i in season:
    if (month_number in season.get(i)) == True:
        print('Данный месяц относится к времени года', i)

