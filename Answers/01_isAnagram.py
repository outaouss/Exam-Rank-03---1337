class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = sorted(s)
        y = sorted(t)
        
        return x == y


# Test cases
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Expected: True
print(solution.isAnagram("jar", "jam"))           # Expected: False
