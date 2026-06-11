"""
Exercise: Pattern Tracker
=========================

Given a string text, count the number of times two consecutive digits
appear where the second digit is exactly 1 more than the first.

Examples:
---------
Input:  "12a34"
Output: 2

Input:  "1234"
Output: 3

Input:  "9087"
Output: 0

Constraints:
------------
- The string may contain any characters (letters, digits, symbols).
- Only digit-digit pairs are considered.
"""


def pattern_tracker(text: str) -> int:

    count = 0

    i = 0
    for c in text:
        if c.isdigit():
            try:
                if text[i + 1].isdigit():
                    if int(c) + 1 == int(text[i + 1]):
                        count += 1
            except IndexError:
                pass
        i += 1
    return count


# Test cases
print(pattern_tracker("12a34"))  # Expected: 2
print(pattern_tracker("1234"))   # Expected: 3
print(pattern_tracker("9087"))   # Expected: 0
