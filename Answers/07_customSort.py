def custom_sort(arr: list) -> list:
    
    vowels = "aeiou"
    
    return sorted(arr, key=lambda i: (len(i), i.lower(), sum(1 for c in i if c.lower() in vowels), arr.index(i)))


# Test cases
print(custom_sort(["Apple", "bZPLE", "BZPLE", "chor"]))
# Expected: ["chor", "BZPLE", "bZPLE", "Apple"]
