def check_prime(x):
    y = x//2
    while(y > 1):
        if(x % y == 0):
            print "%s has factors" %x
            break
        y -= 1
    else:
        print "%s is a prime number" %x
        

check_prime(5)