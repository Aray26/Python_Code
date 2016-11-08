from abc import ABCMeta, abstractmethod
import os

class Enemy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def attackPlayer(self, player):
        pass

class EnvironmentAsset(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self):
        self.mobile = False

class Trap(Enemy, EnvironmentAsset):
    '''
    trap some cash
    '''
    def __init__(self):
        super(Trap,self).__init__()
    
    def attackPlayer(self, player):
        player.health = 40
        return player.health

class Player(object):
    def __init__(self, name):
        self.health = 10
        self.name = name 

player = Player("Gary")        
x = Trap()

print player.name
print player.health

print x.attackPlayer(player)


print abs.__doc__

print "Enemy is first, the EnvironmentAsset - it is called Method Resolution Order MRO"

print Player.mro()
print Player.__mro__

print Trap.mro()
print Trap.__mro__
print Trap.__doc__
d = "dog"
print d.__doc__
