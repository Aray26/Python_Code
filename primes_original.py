import math

n=int(math.sqrt(600851475143) )+1

for p in range(2, n+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print p,
print 'Done'