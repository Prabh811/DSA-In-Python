
def leaders(arr):

    # Method 1
    # time complexity = O(n)
    # space complexity = O(n)

    if not arr:
        return None
    res = []
    leader = len(arr) - 1
    res.append(arr[leader])

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > arr[leader]:
            res.append(arr[i])
            leader = i
    return res

arr = list(map(int, input().split()))
print(leaders(arr))