"""
Exercise: Valid Parentheses
===========================

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Examples:
---------
Input:  s = "()"
Output: True

Input:  s = "()[]{}"
Output: True

Input:  s = "[(])"
Output: False

Input:  s = "{[]}"
Output: True

Constraints:
------------
- 1 <= s.length <= 10^4
- s consists of parentheses only: '()[]{}'
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pass


# Test cases
solution = Solution()
print(solution.isValid("()"))      # Expected: True
print(solution.isValid("()[]{}"))  # Expected: True
print(solution.isValid("[(])"))    # Expected: False
print(solution.isValid("{[]}"))    # Expected: True
