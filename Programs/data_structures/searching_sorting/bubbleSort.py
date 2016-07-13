def bubbleSort(items):
    iterations = len(items) -1
    while iterations:
        for i in range(iterations):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
        iterations -= 1
    return items
    


items = [15, 70, 23, 44, 16, 99, 66, 32]
print bubbleSort(items)
###O(nsquare)