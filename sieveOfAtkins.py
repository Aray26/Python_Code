import math


def sieveOfAtkin(limit):
    total = 0
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P
#total=0
print sieveOfAtkin(2000000)

#print sieveOfAtkin(10000000000)
#10 000 000 000

#total += sieveOfAtkin(2000000)
total = sum(sieveOfAtkin(2000000))
#total = sum(sieveOfAtkin(10000000000))
print "total is " + str(total)