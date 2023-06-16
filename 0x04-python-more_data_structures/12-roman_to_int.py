#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    s = roman_string
    intger = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
            intger -= roman[s[i]]
        else:
            intger += roman[s[i]]
    return intger
