def left_rotate_one(arr):
    
    temp = arr[0]
    
    for i in range(1,len(arr)):
        arr[i - 1] = arr[i]
        
    arr[len(arr) - 1] = temp
    
    return arr
    
# print(left_rotate_one([1,2,3,4,5]))
print(left_rotate_one([30, 5, 20]))
    