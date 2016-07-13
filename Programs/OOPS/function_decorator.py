class FunctionDecorator:
    def __init__(self, function):
        self.counter = 0
        self.function = function
    def __call__(self, *args):
        self.counter += 1
        print "number of calls made to decorator {}" .format(self.counter)
        self.function(*args)

@FunctionDecorator
def sample_function(a, b, c):
    print(a, b, c)
    
sample_function(1, 2, 3)
sample_function('a', 'b', 'c')