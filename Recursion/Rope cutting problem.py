
def max_pieces(n, a, b, c):

    # time complexity = O(3^n)

    if n == 0:
        return 0
    if n < 0:
        return -1
    
    res = max(max_pieces(n - a, a, b, c), max_pieces(n - b, a, b, c), max_pieces(n - c, a, b, c))

    if res == -1:
        return -1
    return res + 1

n = int(input())
a = int(input())
b = int(input())
c = int(input())

print(max_pieces(n, a, b, c))