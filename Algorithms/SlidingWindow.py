def fixed_sliding_window(arr: List[int], k: int) -> List[int]:
    # sum of first subarray and add it to the result
    curr_subarray = sum(arr[:k])
    result = [curr_subarray]

    # To get each subsequent subarray, add next value in list, and remove first value
    for i in range(1, len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1] + arr[i+k-1]
        result.append(curr_subarray)

    return result

def dynamic_sliding_window(arr: List[int], x: int) -> List[int]:
    # Track minimum value
    min_length = float('inf')

    # The current range and sum of our sliding window
    start, end, curr_sum = 0, 0, 0
    # Extend the sliding window until our criteria is met
    while end < len(arr):
        curr_sum = curr_sum + arr[end]
        end += 1
        # Then contract the sliding window until it no longer meets condition
        while start < end and curr_sum >= x:
            curr_sum = curr_sum - arr[start]
            start += 1
            
            # Update the min_length if this is shorter than the current min
            min_length = min(min_length, end-start+1)

    return min_length