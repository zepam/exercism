# inspired by glennj
from math import floor, ceil

def smallest(max_factor, min_factor):
    validate(min_factor, max_factor)
    factors = range(min_factor, max_factor + 1)
    # start with smallest and work up
    products = range(pow(min_factor, 2), pow(max_factor, 2) + 1)
    # send over all factors, but it will return just pairs
    return palindrome_products(products, factors)

def largest(max_factor, min_factor):
    validate(min_factor, max_factor)
    factors = range(min_factor, max_factor + 1)
    # start with largest and work down
    products = range(pow(max_factor, 2), pow(min_factor, 2) - 1, -1)
    # send over all factors, but it will return just pairs
    return palindrome_products(products, factors)

def validate(minf, maxf):
    if minf > maxf:
        raise ValueError('min must be <= max')

def palindrome_products(products, factors):
    for product in products:
        if is_palindrome(product):
            pairs = []
            for i in factors:
                # j = quotient, rem = remainder
                j, rem = divmod(product, i)
                if rem == 0 and j in factors:
                    pairs.append([i, j])
            if len(pairs) != 0:
                # the first one found is the smallest/largest,
                # so we can return immediately
                return (product, pairs)
    return (None, [])


def is_palindrome(number):
    s = str(number)
    return s == s[::-1]
