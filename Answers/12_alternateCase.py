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
    
    i = 0
    new = ""
    for c in string:
        if c.isalpha():
            if i % 2 == 0:
                c = c.upper()
            else:
                c = c.lower()
            new += c
            i += 1
        else:
            new += c
    return new    


# Test cases
print(alternate_case("hello world!"))
print(alternate_case("abc"))
print(alternate_case("a1b2c"))
