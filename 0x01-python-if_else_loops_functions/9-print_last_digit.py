#!/usr/bin/python3
def print_last_digit(number):
    last_digit = ""
    if number < 0:
        last_digit = number % -(10)
        print("{}".format(-(last_digit)), end="")
    else:
        last_digit = number % 10
        print("{}".format(last_digit), end="")
    return abs(last_digit)
