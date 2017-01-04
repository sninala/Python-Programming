def mergeSort(items):
    '''
    --divide and conquer strategy
    recursive algorithm that continually splits a list into half
     If the list is empty or has one item, it is sorted by definition
     If the list has more than one item, we split the list and recursively invoke a merge sort on both halves.
     Once the two halves are sorted, the fundamental operation, called a merge, is performed. 
    '''
    totalElements = len(items)
    if(totalElements > 1):
        mid = totalElements//2
        lefthalf = items[:mid]
        righthalf = items[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i,j,k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k] = lefthalf[i]
                i += 1
            else: 
                items[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1
    return items


items = [15, 70, 23, 44, 16, 99, 66, 32]
print mergeSort(items)