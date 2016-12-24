class Worker(object):


    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    
    def getName(self):
        return self.name
    
worker1 = Worker('Siva Ninala', 30000)
print worker1.getName()