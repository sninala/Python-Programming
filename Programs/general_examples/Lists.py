### ordered collection and mutable
L = [1, 2, 3, 4]
L1 = ['abc', ['def', 'ghi']]
L2 = list('spam')
L3 = list(range(-4, 4))
print L, L1, L2, L3

L.append(5)
L.extend([5, 6, 7, 8, 9])
L.insert(0, 0)
print L
L.reverse()
print L
del L[3]
del L[3:5]
L.remove(8)
print L
print [x**2 for x in L] ## List comprehension
## Iteration
for x in [1, 2, 3]:
    print(x) 
## Matrix 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
