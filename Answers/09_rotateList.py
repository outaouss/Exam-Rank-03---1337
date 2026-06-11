"""
Exercise: Rotate List
=====================

Given a list li and an integer k, rotate the list to the right by k steps.

Rotating to the right means taking the last element and moving it to the front.

Examples:
---------
Input:  li = [1, 2, 3, 4], k = 2
Output: [3, 4, 1, 2]

Input:  li = [1, 2, 3], k = 1
Output: [3, 1, 2]

Input:  li = [1, 2, 3, 4, 5], k = 3
Output: [3, 4, 5, 1, 2]
"""

def rotateList(li: list, k: int) -> list:
    
    for _ in range(k):
        x = li.pop()
        li.insert(0, x)
    return li


# Test cases
print(rotateList([1, 2, 3, 4], 2))      # Expected: [3, 4, 1, 2]
print(rotateList([1, 2, 3], 1))          # Expected: [3, 1, 2]
print(rotateList([1, 2, 3, 4, 5], 3))   # Expected: [3, 4, 5, 1, 2]
