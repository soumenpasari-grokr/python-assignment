'''
quick sort implementation
'''
def quick_sort(array,first,last):
    if first >= last:
        return
    
    pivotPosition = partition(array,first,last)

    quick_sort(array,first,pivotPosition-1)
    quick_sort(array,pivotPosition + 1,last)

def partition(array,start,end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[low] <= pivot:
            low = low + 1
        while low <= high and array[high] >= pivot:
            high = high - 1
        
        if low <= high :
            array[low],array[high] = array[high],array[low]
        else:
            break
    
    array[start],array[high] = array[high],array[start]

    return high