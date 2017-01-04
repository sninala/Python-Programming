
###classic classes, search procedure is strictly depth first
class A: #classic class
    attr = 1
class B(A): # B and C both lead to A
    pass
class C(A):
    attr = 2
class D(B, C):
    pass # Tries A before C

x = D()
print x.attr


class A1(object): # New-style
    attr = 1
class B1(A1):
    pass
class C1(A1):
    attr = 2
class D1(B1, C1):
    pass # Tries C before A
y = D1()
print y.attr