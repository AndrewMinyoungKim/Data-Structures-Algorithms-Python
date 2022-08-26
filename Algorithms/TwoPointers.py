# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum

# Method


def isPairSum(A, N, X):

    for i in range(N):
        for j in range(N):

            # as equal i and j means same element
            if (i == j):
                continue

            # pair exists
            if (A[i] + A[j] == X):
                return True

            # as the array is sorted
            if (A[i] + A[j] > X):
                break

    # No pair found with given sum
    return 0


# Driver code
arr = [2, 3, 5, 8, 9, 10, 11]
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9

# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

# Method


def isPairSum(A, N, X):

    # represents first pointer
    i = 0

    # represents second pointer
    j = N - 1

    while (i < j):

        # If we find a pair
        if (A[i] + A[j] == X):
            return True

        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif (A[i] + A[j] < X):
            i += 1

        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return 0


# array declaration
arr = [2, 3, 5, 8, 9, 10, 11]

# value to search
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9.
