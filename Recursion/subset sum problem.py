
def subset_sum(arr, n, sum_):

    # Time complexity = O(2^n)
    # space complexity = O(n)
    if n == 0:
        if sum_ == 0:
            return 1
        return 0
    return subset_sum(arr, n - 1, sum_) + subset_sum(arr, n - 1, sum_ - arr[n - 1])

arr = list(map(int, input().split()))
sum_ = int(input())
print(subset_sum(arr, len(arr), sum_))