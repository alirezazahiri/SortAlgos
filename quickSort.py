def partition(start, end, list: list):
    
    pivot_index = start
    pivot = list[pivot_index]
    
    while start < end:
        
        while start < len(list) and list[start] <= pivot:
            start += 1
        
        while list[end] > pivot:
            end -= 1
        
        if(start < end):
            list[start], list[end] = list[end], list[start]
    
    list[end], list[pivot_index] = list[pivot_index], list[end]
    
    return end
     
def quickSort(start, end, list: list, key=''):
     
    if (start < end):
        p = partition(start, end, list)
        
        quickSort(start, p - 1, list)
        quickSort(p + 1, end, list)
    
    if key.casefold() == 'reverse':
        list.reverse()
    
    return list