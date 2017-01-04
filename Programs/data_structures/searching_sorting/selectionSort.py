#selection sort improves on the bubble sort by making only one exchange for every pass through the list

def selectionSort(items):
    iterations = len(items) -1
    while iterations:
        maxValuePosition = 0
        for current_position in range(1, iterations+1):
            if items[current_position] > items[maxValuePosition]:
                maxValuePosition = current_position
        temp = items[iterations]
        items[iterations] = items[maxValuePosition]
        items[maxValuePosition] = temp
        iterations -= 1
    return items
    


items = [15, 70, 23, 44, 16, 99, 66, 32]
print selectionSort(items)
###O(nsquare)