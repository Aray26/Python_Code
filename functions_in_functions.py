print "functions are really just objects \
they can return functions or classes or \
really anything. funtions r objects"

x=7

def printHam():
    pass
    
class Test:
    pass
    
print dir()

def outside():
    def printFuckOff():
        print "Go away"
    print "Is a function obejct " \
    + str(type(printFuckOff))
    return printFuckOff

myComment = outside()
#print type(printFuckOff)
myComment()    

x = 5

def reallyOutside():
    x = 6
    def goOutsideNow():
       print "Going outside"
       print x
    return goOutsideNow
    
y = reallyOutside()

print y()

print "_________________"
def getPassingYards(k):
    yards = 1000
    def getScramblingYards():
        print yards
        print k
        scramblineYards = 22
    return getScramblingYards #this calls inner function
    

yyy = getPassingYards(999)

yyy()


print "_________________"
def getRushingYards(k):
    yards = 1000
    def getPassedYards():
        print yards
        print k
        scramblineYards = 22
    getPassedYards() #this calls inner function
    

yyyw = getRushingYards(999)

print yyyw

