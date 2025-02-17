def sorted_or_not(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True
    
print(sorted_or_not([10, 12, 30, 34, 35]))