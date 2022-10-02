from collections import deque

arr = [0, 1, 2, 3, 4, 5]

# remove first element in 5 different ways
arr.pop(0)
del arr[0]
arr = arr[1:]
arr.remove(arr[0])
arrQ = deque(arr)  # using deque
arrQ.popleft()
print(str(arr))
print(str(list(arrQ)))
