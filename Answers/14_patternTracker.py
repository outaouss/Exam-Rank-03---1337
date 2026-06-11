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
