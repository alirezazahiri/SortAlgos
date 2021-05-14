def bubbleSort(list: list, key='') -> list:

    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    
    if key.casefold() == 'reverse':
        list.reverse()

    return list