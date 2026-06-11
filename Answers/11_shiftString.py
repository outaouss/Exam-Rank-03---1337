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
