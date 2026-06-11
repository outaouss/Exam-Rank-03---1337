class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""
        
        for c in s:
            if c.isalnum():
                new += c
        
        return [new.lower(), new[::-1].lower(), new.lower() == new[::-1].lower()]


# Test cases
solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))  # Expected: True
print(solution.isPalindrome("tab a cat"))                     # Expected: False
print(solution.isPalindrome("non?"))                          # Expected: True
