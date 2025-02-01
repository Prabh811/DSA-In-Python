def recursively_1_to_n(n):
    if n == 0:
        return
    recursively_1_to_n(n - 1)
    print(n, end=" ")
    
recursively_1_to_n(10)