class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        i = 0
        for a in nums:
            j = 0
            for b in nums:
                if a + b == target and i != j:
                    return [j, i]
                i += 1
            j += 1


# Test cases
solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))  # Expected: [0, 1]
print(solution.twoSum([4, 5, 6], 10))    # Expected: [0, 2]
print(solution.twoSum([5, 5], 10))       # Expected: [0, 1]
