class limiter(object):
    __slots__ = ['age', 'name', 'job']

x = limiter()
#x.age # Must assign before use

x.age = 40
print x.age

x.ape = 1000 #AttributeError: 'limiter' object has no attribute 'ape'