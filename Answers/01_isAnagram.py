"""
Exercise: Is Anagram
====================

Given two strings s and t, return True if the two strings are anagrams
of each other, otherwise return False.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Examples:
---------
Input:  s = "racecar", t = "carrace"
Output: True

Input:  s = "jar", t = "jam"
Output: False

Constraints:
------------
- s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)
        
        return x == y


# Test cases
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Expected: True
print(solution.isAnagram("jar", "jam"))           # Expected: False
