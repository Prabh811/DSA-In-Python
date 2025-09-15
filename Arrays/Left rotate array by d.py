
def left_rotate_array(arr, d):

    # Method 1
    # time complexity = O(n)
    # space complexity = O(d)
    temp = []
    for i in range(d):
        temp.append(arr[i])

    i = 0
    for j in range(d, len(arr)):
        arr[i] = arr[j]
        i += 1

    j = 0
    while i < len(arr):
        arr[i] = temp[j]
        j += 1
        i +=1 

    return arr

    # Method 2
    # time complexity = O(n)
    # space complexity = O(1)

    reverse(arr, 0, d - 1)
    reverse(arr, d, len(arr) - 1)
    reverse(arr, 0, len(arr) - 1)

    return arr

def reverse(arr, low, high):
    while low <= high:
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low += 1
        high -= 1


arr = list(map(int, input().split()))
d = int(input())
print(left_rotate_array(arr, d))