def sequentialSearch(items, item):
    index = 0
    found = False
    while(index < len(items) and not found):
        if(items[index] == item):
            found = True
            break
        else:
            index += 1
    
    return found

testlist = [1, 2, 3, 9, 21, 23, 42, 11, 15]

print sequentialSearch(testlist, 3)
print sequentialSearch(testlist, 2)

#the complexity of the sequential search, is O(n)