#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for i in range(len(roman_string)):
        if i > 0 and my_dict[roman_string[i]] > my_dict[roman_string[i - 1]]:
            res += my_dict[roman_string[i]] - 2 * my_dict[roman_string[i - 1]]
        else:
            res += my_dict[roman_string[i]]
    return res
