class Solution:
    def isValid(self, s: str) -> bool:
        
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('()', '')
            s = s.replace('[]', '')

        return s == ""

# Test cases
solution = Solution()
print(solution.isValid("()"))      # Expected: True
print(solution.isValid("()[]{}"))  # Expected: True
print(solution.isValid("[(])"))    # Expected: False
print(solution.isValid("{[]}"))    # Expected: True
