dictt = {'январь': 1, 'февраль':2, 'март' : 3, 'апрель' : 4, 'май' : 5, 'июнь': 6, 'июль' :7, 'август': 8, 'сентябрь' : 9, 'октябрь':10, 'ноябрь':11, 'декабрь':12}

#print( dictt["январь"])
month = dictt[input('введите месяц ')]
#print(month)
day = input ('введите день ')
date = int(str(month)+str(day))
#print (date)
print('знак вашего зодиака:')
if date <= 120 or date >= 1222:
    print('козерог')
if date >= 121 and date <= 218:
    print('водолей')
if date >= 219 and date <= 320:
    print('рыбы')
if date >= 321 and date <=419:
    print('овен')
if date >= 420 and date <= 520:
    print('телец')
if date >=  521 and date <= 621: 
    print ('близнецы')
if date >= 622 and date <= 722: 
    print('рак')
if date >= 723 and date <= 822:
    print('лев')
if date >= 823 and date <= 922:
    print ('дева')
if date >= 923 and date <= 1023:
    print('весы')
if date >= 1024 and date <= 1122:
    print('скорпион')
if date >= 1123 and date <= 1221:
    print('стрелец')
