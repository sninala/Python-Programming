
class newClass(object):
    _age = 0
    def getage(self):
        return self._age
    def setage(self, value):
        print('set age:', value)
        self._age = value
        
    age = property(getage, setage, None, None)# get, set, del, docString
    
a = newClass()
print a.age
a.age = 50
print a.age


