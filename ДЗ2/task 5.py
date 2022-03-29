#Реализовать рейтинг

ranking = [7, 5, 3, 2]
num = int(input('ВВедите число: '))
ranking.append(num)
ranking.sort(reverse = True)
print(ranking)
