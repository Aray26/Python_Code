print "singletons what what"

class MySingleton(object):
    _instace = None
    def __new__(self):
        if not self.instance:
            self._instace = 