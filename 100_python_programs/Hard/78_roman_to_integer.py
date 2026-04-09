"""
Program: Roman To Integer
Description: Convert Roman numerals to integer.

Hint:
- Scan using value rules.

"""

result = 0

def roman(c):
    if c == "I":
        return 1
    elif c == "V":
        return 5
    elif c == "X":
        return 10
    elif c == "L":
        return 50
    elif c == "C":
        return 100
    elif c == "D":
        return 500
    elif c == "M":
        return 1000
    else:
        return 0


roman_int = input("Enter roman integer: ")

for i in range(len(roman_int)):
    current = roman(roman_int[i])
    if i < len(roman_int) - 1:
        nex_t = roman(roman_int[i + 1])
        if current < nex_t:
            result -= current
        else:
            result += current
    else:
        result += current

print(result)
