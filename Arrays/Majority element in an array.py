
def Majority_element(arr):

    # Method 1
    # time complexity = O(n^2)
    # Space complexity = O(1)

    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count > len(arr) // 2:
            return i
        
    return -1

    # Method 2
    # time complexity = O(n)
    # Space complexity = O(1)

    # It's known as Moore's voting algorithm 

    res = 0
    count = 1

    for i in range(1, len(arr)):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    
    count = 0

    for i in range(len(arr)):
        if arr[res] == arr[i]:
            count += 1

    if count < len(arr) // 2:
        res = -1
    return res

# 8 7 6 8 6 6 6 6 
arr = list(map(int, input().split()))
print(Majority_element(arr))