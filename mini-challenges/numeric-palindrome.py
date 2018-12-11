#!/usr/bin/env python3

def bigpals(digits=3, top=10):
    begin = (10 ** digits) - 1
    end = (10 ** (digits - 1)) - 1

    matches = set()
    for i in range(begin, end, -1):
        for j in range(begin, end, -1):
            prod = i * j
            if str(prod) == str(prod)[::-1]:
                matches.add((prod, max(i,j), min(i,j)))
                break

    matches = list(matches)
    matches.sort(reverse=True)
    return matches[:top]


if __name__ == "__main__":
    import sys

    digits = 3
    if len(sys.argv) > 1:
        digits = int(sys.argv[1])

    for n in bigpals(digits):
        print(n)


