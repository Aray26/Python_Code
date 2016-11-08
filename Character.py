#Let's do another one putting this in another file

class Character(object):
    def __init__(self):
        self.health = 100
        self.weapon = "HammerTime Chop"

if __name__ == '__main__':
    print "Works"
    apple = Character()
    print apple.health
    print apple.weapon

