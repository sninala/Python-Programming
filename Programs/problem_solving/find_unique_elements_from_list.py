L = [1, 1, 2, 3, 3, 4, 5, 6]
print [x for x in L if L.count(x)==1]
print filter(lambda x: L.count(x) == 1, L)
