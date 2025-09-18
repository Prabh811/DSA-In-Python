def sum_of_natural(n):
    if n == 0:
        return 0
    return n + sum_of_natural(n - 1)
    
print(sum_of_natural(15))