"""
Exercise: Convert Base
======================

Given a number n represented as a string in base base_from, convert it
and return its representation as a string in base base_to.

- Supports bases from 2 to 36.
- For bases above 10, use uppercase letters: A=10, B=11, ..., Z=35.
- The input may include a leading '-' for negative numbers.

Examples:
---------
Input:  n = "1010", base_from = 2, base_to = 10
Output: "10"

Input:  n = "255", base_from = 10, base_to = 16
Output: "FF"

Input:  n = "Z", base_from = 36, base_to = 10
Output: "35"

Input:  n = "-11", base_from = 2, base_to = 10
Output: "-3"

Constraints:
------------
- 2 <= base_from, base_to <= 36
- n is a valid number in base_from (may start with '-')
"""


def convert_base(n: str, base_from: int, base_to: int) -> str:

    try:
        int(n, base_from)
    except Exception:
        return "0"

    s = ""

    if n[0] == "-":
        s += '-'
        n = n[1:]

    to_decimal = int(n, base_from)

    if base_to == 10:
        return s + str(to_decimal)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    while to_decimal > 0:
        result += digits[to_decimal % base_to]
        to_decimal //= base_to

    return s + result[::-1]


# Test cases
print(convert_base("10", 10, 2))   # Expected: "10"
print(convert_base("255", 10, 16))   # Expected: "FF"
print(convert_base("Z", 36, 10))     # Expected: "35"
print(convert_base("-11", 2, 10))    # Expected: "-3"
