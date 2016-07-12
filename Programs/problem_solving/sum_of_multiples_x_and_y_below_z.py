def getSumofMultiples_below(x, y, z):
    return sum(filter(lambda t: t % x == 0 or t % y == 0, range(z)))

##Example
print getSumofMultiples_below(3, 5, 1000)