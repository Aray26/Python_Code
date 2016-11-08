class Sport(object):
    def __init__(self):
        self.variable = "Level 10"
        self.teamName = "NONE"

    def __init__(self,name):
        self.variable = "Level 200"
        self.teamName = name
    
    def printBall(self):
        print "We haave a SPORT ball"
        
        
class Football(Sport):
    def __init__(self):
        super(Football, self).__init__()
        #pass#variable = Sport.variable
        
    def __init__(self, name):
        super(Football, self).__init__(name)
    
    
    def __init__(self, name, forgeName):
        super(Football, self).__init__(name)
        forgeName = Forge(forgeNamename)
        #pass#variable = Sport.variable
    
    def printBall(self):
        print "Football ball"
    
class Forge:
    def __init__(self,forgeName):
        self.forgeName = forgeName
        
def main():
    #print Football.variable
    a = Football()
    print a.variable
    a.printBall()

if __name__ == "__main__":
    main()
    
