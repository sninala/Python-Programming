def sequentialSearchOnOrderedList(items, item):
    index = 0
    itemFound = False
    while index < len(items):
        if items[index] == item:
            itemFound = True
            break
        else:
            if items[index] > item:
                break
            else:
                index = index + 1
    
    return itemFound

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(sequentialSearchOnOrderedList(testlist, 3))
print(sequentialSearchOnOrderedList(testlist, 13))