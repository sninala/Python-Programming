from Deque import Deque

def isPolindrome(paramString):
    deque = Deque()
    for char in paramString:
        deque.addFront(char)
    polindromeFlag = True
    
    while deque.size() > 1 and polindromeFlag:
        firstChar = deque.removeFront()
        lastChar = deque.removeRear()
        if(firstChar != lastChar):
            polindromeFlag = False
            break
    
    return polindromeFlag

print isPolindrome('Siva')
print isPolindrome('liril')