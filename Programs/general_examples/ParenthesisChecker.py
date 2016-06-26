from Programs.data_structures import Stack
def ParenthesisChecker(symbolString):
    s = Stack.Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(ParenthesisChecker('((()))'))
print(ParenthesisChecker('(()'))