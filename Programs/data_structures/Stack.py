class Stack:
    def __init__(self):
        '''
        creates a new stack object
        '''
        self.items = []
    
    def isEmpty(self):
        '''
        returns True if Stack is empty, else returns false
        '''
        return self.items == []

    def push(self, item):
        '''
        adds a new item to the top of the stack, returns nothing.
        '''
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    
    
a = Stack()
a.push(1)
a.push(2)
print a.pop()
print a.isEmpty()

# Another Implementation of Stack
class Stack1:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.insert(0, item)
    
    def pop(self):
        return self.items.pop(0)    
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
s = Stack1()
s.push('hello')
s.push('true')
print(s.pop())

