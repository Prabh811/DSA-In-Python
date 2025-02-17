def remove_duplicates(arr):
    
    res = 1
    
    for i in range(len(arr)):
        if arr[i] != arr[res - 1]:
            arr[res] = arr[i]
            res += 1
    return res
    
arr = [10, 20, 20, 30, 30, 30, 30]
res = remove_duplicates(arr)

print(list(arr[i] for i in range(res))) # [10, 20, 30]