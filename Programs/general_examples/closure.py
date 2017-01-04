'''
We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.
'''
###Example 1
def print_msg(msg):
    def printer():
        print msg
    return printer
call = print_msg("siva")
print call.__closure__
call()

## Example 2 

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
times3 = make_multiplier_of(3)
print times3(5)