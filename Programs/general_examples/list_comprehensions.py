L = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in L]
print squares

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
## print diagonal elements of array
diag = [M[i][i] for i in range(len(M))]
print diag

### calculate the sum of each row
S = [sum(row) for row in M]
print S

### calculate the sum of each row and creates a generator object
S = (sum(row) for row in M)
print S

