''' I am thinkign of a 3 digit positive integer. the integer has 12 positive factors. the sum of two of its factors
is 23 and the difference of those two factors is 1 . What is my number"

if a star b is defined as  a* b+3 what is the absoltuie difference between (10 star 11 ) star 12 and 10 star (11 star 12)
http://screengrabber.deadspin.com/espn-aired-a-mathletics-competition-and-it-was-amazing-1775564496



'''

def printme( str ):
   "This prints a passed string into this function"
   print str
   return
   
def calcStar(number1,number2  ):
   "This prints a passed string into this function"
   x = (number1 * number2 ) +3 
   print x 
   return x


printme('Adi')

calcStar(2,2)

calcStar(10,11)

calcStar(calcStar(10,11),12)

calcStar(calcStar(11,12),10)

y = calcStar(calcStar(11,12),10) - calcStar(calcStar(10,11),12)
print abs(y)




def calculateFactors(number):
    countNumberOfFactors=0
    listOfFactors=[]
    for x in range(1,number+1):
        if ((number%x) == 0):
           #print "for the number " + str(number)
           #print "x is a factor "  + str(x)
           countNumberOfFactors +=1    
           listOfFactors.append(x)           
    if (countNumberOfFactors ==12):
       print "NUMBER = " + str(number)
       print "List of factors for " + str(number) + " is " + str(listOfFactors)
       for elementOfArray in listOfFactors:
           for testElementOfArray in listOfFactors:
               if (testElementOfArray == elementOfArray):
                  break
               else:
                  if (testElementOfArray+elementOfArray) == 23:
                     print "WOOOW"
                     if (abs(testElementOfArray-elementOfArray)) == 1:
                        print "Answer is " + str(number)
       #print '\n'.join(str(p) for p in countNumberOfFactors)
       #print(*countNumberOfFactors, sep='\n') 
       #for p in str(countNumberOfFactors):
       #    print str(p)       
    return           
           
for i in range(100,1000):
    #print i
    calculateFactors(i)


    