b = ['emp1', 'emp2', 'emp3']
a = [1,2,3]
D = dict(zip(b, a))
Keys = list(D.keys())
Keys.sort()
for f in Keys:
    print f + ':' + str(D[f])
