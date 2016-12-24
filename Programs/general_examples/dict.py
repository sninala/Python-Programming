#Constructing a dictionary using two lists
b = ['emp1', 'emp2', 'emp3']
a = [1,2,3]
D = dict(zip(b, a))
Keys = list(D.keys())
Keys.sort()
for f in Keys:
    print f + ':' + str(D[f])
    
D = {'a': 1, 'c': 3, 'b': 2}
##print D['f']  //Key Error
if not 'f' in D:
    print('missing')


