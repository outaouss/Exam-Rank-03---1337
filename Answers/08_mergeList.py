def mergeList(l1: list, l2: list) -> list:
    return l1 + l2


# Test cases
print(mergeList([1, 3, 5], [2, 4, 6]))              # Expected: [1, 2, 3, 4, 5, 6]
print(mergeList(["abc", "abd"], ["aad", "zdd"]))    # Expected: ["aad", "abc", "abd", "zdd"]
print(mergeList([], [1, 2]))                         # Expected: [1, 2]
