from operator import mul
from functools import reduce

def multiplyMe(*args):
    return reduce(mul, args)

    
print str(multiplyMe(2,3,10))