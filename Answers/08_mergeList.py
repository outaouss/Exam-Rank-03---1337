"""
Exercise: Merge Two Lists
=========================

Given two lists l1 and l2, merge them into a single sorted list and return it.

The elements in the lists can be of any comparable type (integers, strings, etc.).

Examples:
---------
Input:  l1 = [1, 3, 5], l2 = [2, 4, 6]
Output: [1, 2, 3, 4, 5, 6]

Input:  l1 = ["abc", "abd"], l2 = ["aad", "zdd"]
Output: ["aad", "abc", "abd", "zdd"]

Input:  l1 = [], l2 = [1, 2]
Output: [1, 2]
"""

def mergeList(l1: list, l2: list) -> list:
    return l1 + l2


# Test cases
print(mergeList([1, 3, 5], [2, 4, 6]))              # Expected: [1, 2, 3, 4, 5, 6]
print(mergeList(["abc", "abd"], ["aad", "zdd"]))    # Expected: ["aad", "abc", "abd", "zdd"]
print(mergeList([], [1, 2]))                         # Expected: [1, 2]
