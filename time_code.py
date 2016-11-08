from operator import mul
# from functools import reduce # python3 compatibility

def with_lambda(list):
    reduce(lambda x, y: x * y, list)

def without_lambda(list):
    reduce(mul, list)

def forloop(list):
    r = 1
    for x in list:
        r *= x
    return r

import timeit

a = range(50)
b = range(1,50)#no zero
t = timeit.Timer("with_lambda(a)", "from __main__ import with_lambda,a")
print("with lambda:", t.timeit())
t = timeit.Timer("without_lambda(a)", "from __main__ import without_lambda,a")
print("without lambda:", t.timeit())
t = timeit.Timer("forloop(a)", "from __main__ import forloop,a")
print("for loop:", t.timeit())

t = timeit.Timer("with_lambda(b)", "from __main__ import with_lambda,b")
print("with lambda (no 0):", t.timeit())
t = timeit.Timer("without_lambda(b)", "from __main__ import without_lambda,b")
print("without lambda (no 0):", t.timeit())
t = timeit.Timer("forloop(b)", "from __main__ import forloop,b")
print("for loop (no 0):", t.timeit())



