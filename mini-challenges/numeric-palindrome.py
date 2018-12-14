#!/usr/bin/env python3

def big_palindromes(top=5):
    start = 999
    stop = start - 200 # assumption: palindrome exists that is product of numbers in highest 200

    palindromes = []
    for i in range(start, stop, -1):
        for j in range(i, stop, -1):
            prod = i * j
            if is_pal_str(prod):
            # if is_pal_math(prod):
                palindromes.append((prod, i, j))

    palindromes = sorted(list(palindromes), reverse=True)
    return palindromes[:top]

def is_pal_str(num):
    '''checks if the supplied number is a palindrome by converting the number
       to a string and reversing the string for the comparison'''

    s = str(num)
    # Python trick of -1 slice-step to reverse a string
    return s == s[::-1]

def is_pal_math(num):
    '''checks if the supplied number argument is a palindrome using math 
       to compute the reversed numeric value'''

    remaining_digits = num
    flipped = 0
    # consume from least significant digit to most
    while remaining_digits > 0:
        flipped = (10 * flipped) + (remaining_digits % 10) 
        remaining_digits //= 10
    return flipped == num


for pal, i, j in big_palindromes():
    print("{} = {} * {}".format(pal, i, j))

