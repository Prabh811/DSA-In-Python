def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


print(binary_search([1, 2, 67, 98, 332], 332))