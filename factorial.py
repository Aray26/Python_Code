x = int(raw_input())

def factorial(x):
    y=1
    g=1
    for y in range(x+1):
        if y == 0:
           print "test" #next
        else:
           g *= y
    print g
    
    
    
factorial(x)

