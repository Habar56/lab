number = str(input ())

while len(number) < 4:
    number = '0' + number
print(number)
if number[0] == number [3] and number [1] == number[2]:
    print ('число счастливое')
else:
    print ('число не счастливое')
