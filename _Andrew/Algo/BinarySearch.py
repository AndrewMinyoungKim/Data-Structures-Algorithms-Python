def binary_search(array, target):
    # must be a sorted array or linked list
    if not len(array): return -1

    l, r = 0, len(array)-1

    while(l < r):
        mid = (l+r) / 2
        if(array[mid] == target):
            return mid
        elif(array[mid] < target):
            r = mid
        elif(array[mid] > target):
            l = mid

    return -1