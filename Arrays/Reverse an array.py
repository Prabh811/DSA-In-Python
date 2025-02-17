def reverse_array(arr):
    
    low = 0 
    high = len(arr) - 1
    
    while(low <= high):
        
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        
        low += 1
        high -= 1
    return arr
        
arr = [30, 20, 5]
print(reverse_array(arr))