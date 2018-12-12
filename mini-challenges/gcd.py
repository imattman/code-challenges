#!/usr/bin/env python3

def gcd_euclid(a, b):
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, (a % b)
    return b


def gcd_iter(a, b):
    if a < b:
        a, b = b, a

    # range from the smaller number, b, down to 1
    # looking for a value n that divides into both
    for n in range(b, 0, -1):
        if (a % n == 0) and (b % n == 0):
            return n


# test it out
for a, b in [(18, 12), (10, 2), (11, 12), (14, 35), (105, 1005)]:
    print("({}, {}) -> {}".format(a, b, gcd_euclid(a, b)))
