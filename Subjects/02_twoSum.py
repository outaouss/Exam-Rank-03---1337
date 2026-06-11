"""
Exercise: Two Sum
=================

Given an array of integers nums and an integer target, return the indices
i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j
that satisfy the condition.

Return the answer with the smaller index first.

Examples:
---------
Input:  nums = [3, 4, 5, 6], target = 7
Output: [0, 1]

Input:  nums = [4, 5, 6], target = 10
Output: [0, 2]

Input:  nums = [5, 5], target = 10
Output: [0, 1]

Constraints:
------------
- 2 <= nums.length <= 1000
- -10,000,000 <= nums[i] <= 10,000,000
- -10,000,000 <= target <= 10,000,000
- Only one valid answer exists.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass


# Test cases
solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))  # Expected: [0, 1] or [1, 0]
print(solution.twoSum([4, 5, 6], 10))    # Expected: [0, 2] or [2, 0]
print(solution.twoSum([5, 5], 10))       # Expected: [0, 1] or [1, 0]
