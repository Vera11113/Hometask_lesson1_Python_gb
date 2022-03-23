time_sec = int(input('Введите время в секундах'))
time_hour = time_sec // 3600
time_minute = (time_sec % 3600) // 60
time_sec_formal = time_sec % 3600 % 60
time_day = None
if time_hour > 24:
    time_day = time_hour // 24
    time_hour = time_hour % 24
if (time_day != None):
    if time_hour // 10 == 0:
        if time_minute // 10 == 0:
            if time_sec_formal // 10 == 0:
                print(f'{time_day}:0{time_hour}:0{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_day}:0{time_hour}:0{time_minute}:{time_sec_formal:.0f}')
        else:
            if time_sec_formal // 10 == 0:
                print(f'{time_day}:0{time_hour}:{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_day}:0{time_hour}:{time_minute}:{time_sec_formal:.0f}')
    else:
        if time_minute // 10 == 0:
            if time_sec_formal // 10 == 0:
                print(f'{time_day}:{time_hour}:0{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_day}:{time_hour}:0{time_minute}:{time_sec_formal:.0f}')
        else:
            if time_sec_formal // 10 == 0:
                print(f'{time_day}:{time_hour}:{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_day}:{time_hour}:{time_minute}:{time_sec_formal:.0f}')
else:
    if time_hour // 10 == 0:
        if time_minute // 10 == 0:
            if time_sec_formal // 10 == 0:
                print(f'0{time_hour}:0{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'0{time_hour}:0{time_minute}:{time_sec_formal:.0f}')
        else:
            if time_sec_formal // 10 == 0:
                print(f'0{time_hour}:{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'0{time_hour}:{time_minute}:{time_sec_formal:.0f}')
    else:
        if time_minute // 10 == 0:
            if time_sec_formal // 10 == 0:
                print(f'{time_hour}:0{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_hour}:0{time_minute}:{time_sec_formal:.0f}')
        else:
            if time_sec_formal // 10 == 0:
                print(f'{time_hour}:{time_minute}:0{time_sec_formal:.0f}')
            else:
                print(f'{time_hour}:{time_minute}:{time_sec_formal:.0f}')