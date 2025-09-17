
import math
def Maximum_subarray_sum(arr):

    # Method 1
    # Time complexity = O(n^2)
    # Space complexity = O(1)

    n = len(arr)
    res = arr[0]
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]
            res = max(res, sum_)

    return res

    # Method 2
    # Time complexity = O(n)
    # Space complexity = O(1)

    res = arr[0]
    max_ending = arr[0]

    for i in range(1, len(arr)):
        max_ending = max(max_ending + arr[i], arr[i])
        res = max(res, max_ending)

    return res


arr = list(map(int, input().split()))
print(Maximum_subarray_sum(arr))