n = int(input())
minn = n
dell = n
for i in range (2,n):
    dell = i 
    if n%dell == 0:

        if dell < minn:
            minn = dell
print (minn)