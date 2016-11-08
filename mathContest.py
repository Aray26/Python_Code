from __future__ import division
import math

'''the least positive integer that is divisible by 2,3,4,5 and is a perfect square and a perfect cube, 4th power and 5th pwer
can be written as a^b. what is least possible value of a + b?

answer 90 


'''
def is_perfect_cube(n):
    c = int(n**(1/3.))
    return (c**3 == n) or ((c+1)**3 == n)
    
    
for i in range(1,10000000):
    if (i%2==0):
        if (i%3==0):
           if (i%4==0):
              if (i%5==0):
                  #print i 
                  for x in range(1,i+1):
                      #if (((x*x)/i) == 1):
                      #   print "WOWOW we have perfect square"
                      #   print "x is " + str(x) + " i is " + str(i)
                      #   for y in range(1,i+1):                         
                         #    print "i and 1 " + str(i + 1) 
                             #print y
                             #print x
                             if ((x*x*x)/i == 1):
                                print "NOW we have perfect cube"
                                print i
                                print "y is " + str(x)
                         
                  #x = math.sqrt(i)
                  #if ((x).is_integer() == 'TRUE'):
                  #   print i
                  #   print is_perfect_cube(i)
                  #else:
                     #print "NOOO"