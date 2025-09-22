
def binary_search(arr, low, high, target):

    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

arr = list(map(int, input().split()))
target = int(input())
print(binary_search(arr, 0, len(arr) - 1, target))