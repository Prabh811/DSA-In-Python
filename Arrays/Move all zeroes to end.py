def move_to_zero(arr):
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp = arr[i]
            arr[i] = arr[non_zero]
            arr[non_zero] = temp
            non_zero += 1
            
    return arr
    
# print(move_to_zero([8, 5, 0, 10, 0, 20]))
print(move_to_zero([0, 0, 0, 10,0]))