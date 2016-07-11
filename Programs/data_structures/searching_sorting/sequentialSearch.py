def sequentialSearch(items, item):
    index = 0
    itemFound = False
    while(index < len(items)):
        if(items[index] == item):
            itemFound = True
            break
        else:
            index += 1
    
    return itemFound

testlist = [1, 2, 3, 9, 21, 23, 42, 11, 15]

print sequentialSearch(testlist, 2)
print sequentialSearch(testlist, 10)

#the complexity of the sequential search, is O(n)