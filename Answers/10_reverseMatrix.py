def reverse_matrix(matrix: list) -> list:
    
    tot = []
    for li in matrix:
      tot.append(li[::-1])
    
    return tot


# Test cases
print(reverse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# Expected: [[3, 2, 1], [6, 5, 4], [9, 8, 7]]

print(reverse_matrix([[1, 2], [3, 4]]))
# Expected: [[2, 1], [4, 3]]
