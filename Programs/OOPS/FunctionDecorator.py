class decorate_tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    
    def __call__(self, *args):
        self.calls += 1
        print self.calls
        self.func(*args)

@decorate_tracer
def echo(a, b, c):
    print a, b, c
    
echo(1, 2, 3)
echo(4, 5, 6)
echo(7, 8, 9)