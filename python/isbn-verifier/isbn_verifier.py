import string

def is_valid(isbn):
    isbn_nums = list(isbn.replace("-", ""))
    
    if len(isbn_nums) != 10:    # also checks for empty isbn #s
        return False
    if isbn_nums[-1] == "X":    # replace last X with 10
        isbn_nums[-1] = "10"
    
    if not all(n.isdigit() for n in isbn_nums): # check for non-valid chars
            return False

    isbn_check = 0

    place = 10
    for n in isbn_nums:
        isbn_check += int(n)*place
        place -= 1

    return (isbn_check % 11 == 0)
    
    """
    last_isbn_char = isbn[-1:]
    if last_isbn_char is not ("X" or last_isbn_char.isDigit()):
        return False
    isbn = isbn[:-1]


    # calculate
    isbn_check = 0

    place = 10
    for n in str(isbn):
        m = int(n)
        isbn_check += m*place
        place -= 1
    if last_isbn_char == 'X':
        isbn_check += 10
    else:
        isbn_check += int(last_isbn_char)
"""
