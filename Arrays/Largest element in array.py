def largest_element(arr):

    if len(arr) == 0:
        return None

    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            
    return max

try:
    user_input = list(map(int, input().split()))
    print(largest_element(user_input))
except Exception as e:
    print("Try to provide valid inputs")
