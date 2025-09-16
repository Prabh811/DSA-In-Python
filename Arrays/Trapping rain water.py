
def trapping_rain_water(arr):

    # Method 1
    # Time complexity = O(n^2)
    # Space complexity = O(1)

    res = 0

    for i in range(1, len(arr) - 1):

        l_max = arr[i]

        for j in range(0, i):
            l_max = max(l_max, arr[j])

        r_max = arr[i]
        for j in range(i + 1, len(arr)):
            r_max = max(r_max, arr[j])

        res += min(l_max, r_max) - arr[i]

    return res

    # Method 2
    # Time complexity = O(n)
    # Space complexity = O(n)

    res = 0
    n = len(arr)
    l_max = [0] * n
    r_max = [0] * n

    l_max[0] = arr[0]
    for i in range(1, n):
        l_max[i] = max(arr[i], l_max[i - 1])

    r_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        r_max[i] = max(arr[i], r_max[i + 1])

    for i in range(1, n - 1):
        res += min(l_max[i], r_max[i]) - arr[i]

    return res

# 3 0 1 2 5
arr = list(map(int, input().split()))
print(trapping_rain_water(arr))