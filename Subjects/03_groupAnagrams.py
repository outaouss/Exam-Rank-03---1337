"""
Exercise: Group Anagrams
========================

Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Examples:
---------
Input:  strs = ["act", "pots", "tops", "cat", "stop", "hat"]
Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

Input:  strs = ["x"]
Output: [["x"]]

Input:  strs = [""]
Output: [[""]]

Constraints:
------------
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters.
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass


# Test cases
solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
# Expected: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]] (any order)
print(solution.groupAnagrams(["x"]))   # Expected: [["x"]]
print(solution.groupAnagrams([""]))    # Expected: [[""]]
