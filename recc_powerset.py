
# Python3 program to generate power set
def powerSet(string, index, curr):
    # string : Stores input string
    # curr : Stores current subset
    # index : Index in current subset, curr
    if index == len(string):
        print(curr)
        return
    # two situatons"
    # 1. adding other subsets to the current subset
    # 2 . Not doing that.
    powerSet(string, index + 1, curr + string[index])
    powerSet(string, index + 1, curr)


# Driver Code
if __name__ == "__main__":
    s1 = "abcde"
    index = 0
    curr = ""
    powerSet(s1, index, curr)