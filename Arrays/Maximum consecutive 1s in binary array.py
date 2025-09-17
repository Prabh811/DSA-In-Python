
def maximum_consecutive(arr):

    # Time complexity = O(n)
    # Space complexity = O(1)
    count = 0
    res = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0
        elif arr[i] == 1:
            count += 1
            res = max(count, res)
    return res

arr = list(map(int, input().split()))
print(maximum_consecutive(arr))