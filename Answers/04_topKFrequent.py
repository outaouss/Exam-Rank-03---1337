class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        d = {}

        for a in nums:
            if a not in d:
                d[a] = 0

            c = nums.count(a)
            d[a] = c

        return sorted(d, key=d.get, reverse=True)[:k]


# Test cases
solution = Solution()
print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Expected: [2, 3]
print(solution.topKFrequent([7, 7], 1))
