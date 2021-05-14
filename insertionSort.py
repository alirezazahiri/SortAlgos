def insertionSort(list: list, key='') -> list:
    
    for i in range(1, len(list)):
        
        point = list[i]
        j = i-1

        while j >= 0 and point < list[j]:
            list[j + 1] = list[j]
            j -= 1
        
        list[j + 1] = point
    
    if key.casefold() == 'reverse':
        list.reverse()
    
    return list