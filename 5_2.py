n = int(input())
dell = n
minn = n
while dell >= 2:
    if n % dell == 0:
        if minn > dell:
            minn = dell
    dell -= 1 
print (minn)