class Methods(object):
    def imeth(self, x): # Normal instance method: passed a self
        print(self, x)
    @staticmethod
    def smeth(x): # Static: no instance passed
        print(x)
    
    @classmethod
    def cmeth(cls, x): # Class: gets class, not instance
        print(cls, x)

    #smeth = staticmethod(smeth) # Make smeth a static method
    #cmeth = classmethod(cmeth) # Make cmeth a class method
    

obj = Methods()
obj.imeth(1)
Methods.smeth(3)
obj.smeth(4)

Methods.cmeth(5)