
def stock_buy_sell(arr):

    # Time complexity = O(n)
    # Space complexity = O(1)
    profit = 0

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            profit += (arr[i] - arr[i - 1])

    return profit 

# 1 5 3 8 12
arr = list(map(int, input().split()))
print(stock_buy_sell(arr))