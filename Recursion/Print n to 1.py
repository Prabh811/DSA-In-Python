def recursive_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    recursive_n_to_1(n - 1)
    
recursive_n_to_1(int(input()))