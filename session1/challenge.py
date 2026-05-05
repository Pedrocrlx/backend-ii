## Session 1 Challenge with Bubble Sort

def bubble_sort(array:list):
    """Bubble sort algorithm"""
    for i in range(len(array) -1): ## i represent index
        for j in range(len(array) - 1 - i): ## j represent value not index
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] ## change indexes
            continue
    return array

array = [5,3,4,1,2,9,8,6,7]
print(f"Input: {array}")

sorted_array = bubble_sort(array)
print(f"Output: {sorted_array}")