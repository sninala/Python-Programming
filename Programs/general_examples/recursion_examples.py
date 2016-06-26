def calcsum(L):
    if len(L)==1:
        return L[0]
    else:
        return L[0] + calcsum(L[1:])
    
List = range(1,101)
print calcsum(List)

def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number-1)
    
print fact(5)