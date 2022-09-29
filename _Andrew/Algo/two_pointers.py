def two_pointers(arr, target):
    # arr must be already sorted

    l, r = 0, len(arr) - 1

    while(l < r):
        if(arr[l] + arr[r] == target):
            return l, r
        
        elif(arr[l] + arr[r] < target):
            l += 1

        else:
            r -= 1

    return 0