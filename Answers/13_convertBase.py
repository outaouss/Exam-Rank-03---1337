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
