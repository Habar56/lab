n = int(input())
world = ''
if n <= 1 or (n % 100 >20 and n % 10 == 1):
    world = 'корова'
if (n > 1 and n < 5) or (n % 100 >20 and n % 10 >1 and n % 10<5 ):
    world = 'коровы'
if (n>5 and n <10) or n % 10 == 0 or n % 10 > 5:
    world = 'коров'
print ('на лугу пасется '+str(n)+ ' '+ str(world))
print(56%10)