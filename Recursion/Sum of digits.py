def get_sum(n):
    
    if n == 0:
        return 0
    
    return get_sum(n // 10) + n % 10
    
print(get_sum(253))