"""
Exercise: Shift String (Caesar Cipher)
=======================================

Given a string and an integer k, shift every alphabetic character in the
string forward by k positions in the alphabet (wrapping around if necessary).

- Preserve the case of each character (uppercase stays uppercase, lowercase stays lowercase).
- Non-alphabetic characters (spaces, digits, punctuation) are left unchanged.

Examples:
---------
Input:  string = "Hello", k = 1
Output: "Ifmmp"

Input:  string = "xyz", k = 3
Output: "abc"

Input:  string = "Hello, World!", k = 13
Output: "Uryyb, Jbeyq!"

Constraints:
------------
- 0 <= k <= 1000
- The string may contain any printable ASCII characters.
"""


def shift_string(string: str, k: int) -> str:

    new = ""

    for c in string:
        if c.isalpha():
            if c.islower():
                new += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
            else:
                new += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            new += c

    return new


# Test cases
print(shift_string("Hello", 1))          # Expected: "Ifmmp"
print(shift_string("xyz", 3))            # Expected: "abc"
print(shift_string("Hello, World!", 13))  # Expected: "Uryyb, Jbeyq!"
