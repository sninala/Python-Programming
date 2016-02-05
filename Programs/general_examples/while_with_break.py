"""
while True:
    name = input('Enter name:')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age))

"""
n = input("Enter num")
n = int(n)
if n>1:
    for x in range(2, n):
        if(n%x == 0):
            print "%d not a prime", n
            break
    else:
        print "%d is a prime", n
        
else:
    print "%d not a prime", n

