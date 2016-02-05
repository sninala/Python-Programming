def times(x=10, y =20):
    return x * y
L = [5,4]
print times(5,4)
print times(x=5, y=4)
print times(*L)
print times(5)
