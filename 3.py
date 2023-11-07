days = int(input())
if (days % 4 == 0 and days % 100 != 0) or days % 400 == 0:
    print ('Yes')
else:
    print ('No')