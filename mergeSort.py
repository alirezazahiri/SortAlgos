def mergeSort(list: list, key='') -> list:
    n = len(list)

    if n <= 1:
        return list
    
    mid = n // 2

    L = mergeSort(list[:mid])
    R = mergeSort(list[mid:])

    return merge(L, R, key)


def merge(list_one: list, list_two: list, key='') -> list:
    list = []

    while len(list_one) > 0 and len(list_two) > 0:
        if list_one[0] < list_two[0]:
            list.append(list_one[0])
            list_one.pop(0)
        else:
            list.append(list_two[0])
            list_two.pop(0)
    
    list += list_one
    list += list_two

    if key.casefold() == 'reverse':
        list.reverse()

    return list
