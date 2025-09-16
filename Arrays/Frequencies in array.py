
def frequency(arr):

    # Method 1
    # Time complexity = O(n)
    # space complexity = O(n)

    if len(arr) <= 0:
        return None
    
    freq_dict = {}

    for ele in arr:
        if ele in freq_dict:
            freq_dict[ele] += 1
        else:
            freq_dict[ele] = 1

    return freq_dict

    # Method 2
    # Time complexity = O(n)
    # Space complexity = O(1)

    freq = 1
    i = 1
    n = len(arr)

    while i < n:
        while i < n and arr[i] == arr[i - 1]:
            freq += 1
            i += 1
        print(arr[i - 1], freq)

        i += 1
        freq = 1

    if n == 1 or arr[n - 1] != arr[n - 2]:
        print(arr[n - 1], 1)

# 10 10 10 30 40 40
arr = list(map(int, input().split()))
print(frequency(arr))