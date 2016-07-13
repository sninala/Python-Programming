def binarySearch(items, item):
    if(len(items) == 0):
        return False
    else:
        middleElement = len(items)//2
        if(items[middleElement] == item):
            return True
        else:
            if(item > items[middleElement]):
                return binarySearch(items[middleElement+1:], item)
            else:
                return binarySearch(items[:middleElement-1], item)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))

#O(log n)