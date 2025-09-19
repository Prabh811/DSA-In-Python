
def subsets(string, curr, i):

    # Time complexity = O(2^n * n)
    # Space complexity = O(n)

    if i == len(string):
        print(curr)
        return

    subsets(string, curr, i + 1)
    subsets(string, curr + string[i], i + 1)

string = input()
subsets(string, "", 0)