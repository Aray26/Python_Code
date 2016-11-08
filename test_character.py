class Character(object):
    def __init__(self,name_of_country):
        self.health = 100
        self.name_of_country = name_of_country
    
    def nameCountry(self):
        print self.name_of_country

class Blacksmith(Character):
    def __init__(self,name_of_country, weapon):
        super(Blacksmith, self).__init__(name_of_country)
        print "incoming " + str(weapon)
        self.weapon = Selectu(weapon)
        print "iii" + str(weapon)
        
    def printBall(self):
        print "Blacksmith " + str(self.name_of_country)
    
    def printWeapon(self):
        print self.weapon

class Selectu():
    def __init__(self,weapon):
        self.weapon = weapon
        print "NOw here " + str(weapon)
         
def main():
    pass
    #print Football.variable
    a = Blacksmith("Inida","knife")
    print a.health
    a.printBall()
    a.printWeapon()
    a.nameCountry()
    print "PPPPP " + str(a.weapon.weapon)

if __name__ == "__main__":
    main()