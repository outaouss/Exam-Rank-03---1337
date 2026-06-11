class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        ang = {}
        
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in ang:
                ang[key] = []
            ang[key].append(word)
        
        return list(ang.values())


# Test cases
solution = Solution()
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
# Expected: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]] (any order)
print(solution.groupAnagrams(["x"]))   # Expected: [["x"]]
print(solution.groupAnagrams([""]))    # Expected: [[""]]
