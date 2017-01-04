#Constructing a dictionary using two lists
b = ['emp1', 'emp2', 'emp3']
a = [1,2,3]
D = dict(zip(b, a))
Keys = list(D.keys())
Keys.sort()
for f in Keys:
    print f + ':' + str(D[f])

##unordered collections; items are stored and fetched by key, instead of by positional offset
    
D = {'a': 1, 'c': 3, 'b': 2}
##print D['f']  //Key Error
if not 'f' in D:
    print('missing')

D = {'spam': 2, 'eggs': 3}
print D.get('eggs')
D.pop('eggs')
print D
D = dict.fromkeys(['a', 'b'])
print D

D = {x: x*2 for x in range(10)} ###Dictionary comprehensions
print D

