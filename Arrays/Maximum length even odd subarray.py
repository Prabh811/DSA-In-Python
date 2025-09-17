
def max_length(arr):

    # Method 1
    # Time complexity = O(n^2)
    # Space complexity = O(1)

    # res = 1
    # for i in range(len(arr)):

    #     curr = 1

    #     for j in range(i + 1, len(arr)):
    #         if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
    #             curr += 1
    #         else:
    #             break

    #     res = max(res, curr)

    # Method 2
    # Time complexity = O(n)
    # Space complexity = O(1)

    res = 1
    curr = 1

    for i in range(1, len(arr)):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1

    return res

# 5 10 20 6 3 8
arr = list(map(int, input().split()))
print(max_length(arr))