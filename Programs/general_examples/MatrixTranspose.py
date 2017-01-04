m = [[1,2],[3,4],[5,6]]
n = []
for i in range(len(m[0])):
    row =[]
    for j in range(len(m)):
        row.append(m[j][i])
    n.append(row)
for row in n:
    print row
## using list comprehension

rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for row in rez:
    print row