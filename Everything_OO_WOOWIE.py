from Character import Character
#My guess is that you have a module called Obstacle, and a class called
#Obstacle, and you have mixed them up. Maybe you are doing this:

#Simple Example
#Here we got the base class - OBJECT!!!!! was the key
class BaseClass(object):
    def printHam(self):
        print 'Ham'
    def printCheese(self):
        print "Cheese"

#the inheriting class doesn't do anything
class InheritingClass(BaseClass):
    pass

#create an example of the child class called x
#call the parent class - methods
x = InheritingClass()
x.printHam()
x.printCheese()


print "++++++++++++++++++++++++++"

#Let's do another one putting this in another file called Character
#class Character(object):
#    def __init__(self):
#        self.health = 100
#        self.weapon = "HammerTime Chop"


class Blacksmith(Character):
    pass
    #def __init__(self):
    #    super(Blacksmith, self).__init__()
    #    self.popp = "poop"
'''

bs = Blacksmith()

print bs.health
print bs.popp


class Thief(Character):
    def __init__(self):
        self.name = "Thief poop"
        super(Thief, self).__init__()


th = Thief()

print th.name

# create barber, then hero as abstract character
# then sorceress, archer,  ugly
# class barber()

# character constructor with slef, name
# def __init__(self,name)
# and jut self - multiple constructors

# then give blacksmith construstor special extra



# multiple inhertitance in Python??????

# base claas in other file

# print BaseClass.__subclasses__()

'''

