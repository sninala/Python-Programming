class SuperClass:
    numberOfInstances = 0
    def __init__(self):
        SuperClass.numberOfInstances += 1

    @staticmethod
    def printNumberOfInstances():
        print "Number of instances {}".format(SuperClass.numberOfInstances)
    @classmethod
    def printInstances(cls):
        print "Number of instances {}".format(SuperClass.numberOfInstances)

"""a = SuperClass()
b = SuperClass()
c = SuperClass()
SuperClass.printNumberOfInstances()"""

class SubClass(SuperClass):
    @staticmethod
    def printNumberOfInstances():
        print "In Subclass"
        SuperClass.printInstances()

a = SubClass()
b = SubClass()
SubClass.printNumberOfInstances()
SuperClass.printNumberOfInstances()
    