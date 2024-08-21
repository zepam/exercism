"""
sublist evaluation
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):

    if len(list_one) == len(list_two):
        if list_one == list_two:
            return EQUAL
        return UNEQUAL
    # if set(list_one) < set(list_two):
    if set(list_one).issubset(set(list_two)):
        return SUBLIST
    if set(list_one).issuperset(set(list_two)):
        return SUPERLIST
    return UNEQUAL
