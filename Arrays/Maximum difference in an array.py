
def maximum_difference(arr):

    # Method 1
    # Time complexity = O(n^2)
    # Space complexity = O(1)

    if len(arr) <= 1:
        return None
    res = arr[1] - arr[0]
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            res = max(res, arr[j] - arr[i])
    return res

    # Method 2
    # Time complexity = O(n)
    # space complexity = O(1)

    if len(arr) <= 1:
        return None
    
    res = arr[1] - arr[0]
    min_val = arr[0]

    for j in range(1, len(arr)):
        res = max(res, arr[j] - min_val)
        min_val = min(min_val, arr[j])

    return res

arr = list(map(int, input().split()))
print(maximum_difference(arr))