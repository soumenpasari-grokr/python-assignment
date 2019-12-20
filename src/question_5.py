'''
question number 5
binary search and return key of searched element
'''
from quicksort import quick_sort

'''
implementation binary search algorithm
and returning the key of found element from
a given list

@param list array - list to be searched in
@param int element - element of the list to be searched

@return int - key of the found element from the list
'''
def custom_search(array,element):
    return binary_search(array,0,len(array)-1,element)

def binary_search(array,first,last,element):
    if element in array:
        if last >= first:
            # getting the mid point
            mid = (first + last) // 2
            #print(mid)
            if array[mid] == element:
                return mid
            elif array[mid] > element:
                return binary_search(array,first,mid-1,element)
            else :
                return binary_search(array,mid+1,last,element)
        else:
            return 'Element not found at last!'
    else:
        return 'Element not found!'

array_to_list = [12,23,34,2,4]

quick_sort(array_to_list,0,len(array_to_list)-1)

element_to_search = 23

# searching element and returning key
element_key = custom_search(array_to_list,element_to_search)

print(element_key)