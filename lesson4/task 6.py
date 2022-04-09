from itertools import count, cycle
from sys import argv

num, start_number, breaking_number = argv
for i in count(int(start_number)):
    if i > 10:
        break
    else:
        print(i)

c = 0
for i in cycle ('Hello'):
    if c > int(breaking_number):
        break
    print(i)
    c += 1


