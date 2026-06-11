def rotateList(li: list, k: int) -> list:
    
    for _ in range(k):
        x = li.pop()
        li.insert(0, x)
    return li


# Test cases
print(rotateList([1, 2, 3, 4], 2))      # Expected: [3, 4, 1, 2]
print(rotateList([1, 2, 3], 1))          # Expected: [3, 1, 2]
print(rotateList([1, 2, 3, 4, 5], 3))   # Expected: [3, 4, 5, 1, 2]
