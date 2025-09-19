
def ToH(n, A, B, C):

    # Think in terms of n = 3
    if n == 1:
        print(A + " to " + C)
        return
    
    ToH(n - 1, A, C, B)
    print(A + " to " + C)
    ToH(n - 1, B, A, C)


n = int(input())
ToH(n, 'A', 'B', 'C')