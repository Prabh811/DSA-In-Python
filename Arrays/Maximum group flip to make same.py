
def maximum_flip(arr):

    # Time complexity = O(n)
    # space complexity = O(1)
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print("From " + str(i) + " to ",end="")
            else:
                print(str(i - 1) + "\n")

    if arr[len(arr) - 1] != arr[0]:
        print(str(len(arr) - 1) + "\n")

# 0 0 1 1 0 0 1 1 0 1
arr = list(map(int, input().split()))
print(maximum_flip(arr))