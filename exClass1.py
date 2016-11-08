class BaseClass(object):
   def printHam(self):
       print 'Ham'
       
class InheritingClass(BaseClass):
    pass
    
x = InheritingClass()
x.printHam()

class Character(object):
    def __init__(self):
        self.health = 100

class Blacksmith(Character):
    def __init__(self):
        super(Blacksmith, self).__init__()
        self.popp = "poop"    
        
bs = Blacksmith()

print bs.health
print bs.popp


class Thief(Character):
    def __init__(self):
       self.name = "Thief poop"
       super(Thief, self).__init__()
       
th = Thief()

print th.name

#create barber, then hero as abstract character
#then sorceress, archer,  ugly
#class barber()

#character constructor with slef, name
#def __init__(self,name)
# and jut self - multiple constructors

#then give blacksmith construstor special extra



#multiple inhertitance in Python??????

#base claas in other file

#print BaseClass.__subclasses__()



