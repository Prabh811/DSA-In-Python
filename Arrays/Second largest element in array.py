def second_largest(arr):
    
    if len(arr) < 2:
        return None
    
    sec_max = float('-inf')
    maximum = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            sec_max = maximum
            maximum = arr[i]
        elif arr[i] >= sec_max and arr[i] < maximum:
            sec_max = arr[i]
            
    if sec_max == float('-inf'):
        return None
    return sec_max
            
        
print(second_largest([10, 7, 10])) 