def remove_duplicate(arr, length):
    if len(arr) <= 0:
        return None
    size = 0
    for i in range(1, length):
        if arr[size] != arr[i]:
            size += 1
            arr[size] = arr[i]
    return arr, size + 1


# 10 20 20 30 30 30
arr = list(map(int, input().split()))
print(remove_duplicate(arr, len(arr)))