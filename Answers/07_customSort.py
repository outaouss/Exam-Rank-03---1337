"""
Exercise: Custom Sort
=====================

Given a list of strings, sort it using the following priority rules:
  1. Primary:   Sort by length (shortest first)
  2. Secondary: Sort alphabetically (case-insensitive)
  3. Tertiary:  Sort by number of vowels (fewest first)

Vowels are: a, e, i, o, u (case-insensitive)

Examples:
---------
Input:  ["Apple", "bZPLE", "BZPLE", "chor"]
Output: ["chor", "BZPLE", "bZPLE", "Apple"]
"""

def custom_sort(arr: list) -> list:
    
    vowels = "aeiou"
    
    return sorted(arr, key=lambda i: (len(i), i.lower(), sum(1 for c in i if c.lower() in vowels), arr.index(i)))


# Test cases
print(custom_sort(["Apple", "bZPLE", "BZPLE", "chor"]))
# Expected: ["chor", "BZPLE", "bZPLE", "Apple"]
