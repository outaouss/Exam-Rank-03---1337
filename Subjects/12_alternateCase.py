"""
Exercise: Alternate Case
========================

Given a string, return a new string where the case of each alphabetic
character alternates: the first letter is uppercase, the second is lowercase,
the third is uppercase, and so on.

Non-alphabetic characters (spaces, digits, punctuation) are kept as-is
and do NOT count as a step in the alternation — only letters affect the toggle.

Examples:
---------
Input:  "hello world!"
Output: "HeLlO wOrLd!"

Input:  "abc"
Output: "AbC"

Input:  "a1b2c"
Output: "A1B2C"
"""

def alternate_case(string: str) -> str:
    pass


# Test cases
print(alternate_case("hello world!"))  # Expected: "HeLlO wOrLd!"
print(alternate_case("abc"))           # Expected: "AbC"
print(alternate_case("a1b2c"))         # Expected: "A1B2C"
