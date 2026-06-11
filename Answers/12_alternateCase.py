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
