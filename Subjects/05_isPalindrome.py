"""
Exercise: Valid Palindrome
==========================

Given a string s, return True if it is a palindrome, otherwise return False.

A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Examples:
---------
Input:  s = "Was it a car or a cat I saw?"
Output: True

Input:  s = "tab a cat"
Output: False

Constraints:
------------
- 1 <= s.length <= 1000
- s is made up of only printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass


# Test cases
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))  # Expected: True
print(solution.isPalindrome("tab a cat"))                     # Expected: False
print(solution.isPalindrome("non?"))                          # Expected: True
