"""
Exercise: Reverse Matrix Rows
==============================

Given a 2D matrix (list of lists), reverse each row of the matrix in place
and return the result.

Examples:
---------
Input:
  [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]

Output:
  [[3, 2, 1],
   [6, 5, 4],
   [9, 8, 7]]

Input:
  [[1, 2],
   [3, 4]]

Output:
  [[2, 1],
   [4, 3]]
"""

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
