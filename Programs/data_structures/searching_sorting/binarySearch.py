def binarySearch(items, item):
    firstItem = 0
    lastItem = len(items) - 1
    itemFound = False
    while(firstItem <= lastItem):
        middleItem  = (firstItem + lastItem)//2
        if(items[middleItem] == item):
            itemFound = True
            break
        else:
            if(item > items[middleItem] ):
                firstItem = middleItem + 1
            else:
                lastItem = middleItem - 1
                
    return itemFound

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
