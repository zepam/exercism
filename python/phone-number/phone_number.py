import re

class PhoneNumber:
    def __init__(self, number):
        SYMBOLS = '+()-. '
        # strip out all acceptable symbols
        for c in SYMBOLS:
            number = number.replace(c,'')

        number = self.validate_quality(number)
        self.validate_structure(number) # doesn't change number, just faults
        self.number = number
        self.area_code = number[0:3]

    def validate_structure(self, number):
        # if a phone number has an exchange code that starts with 0.
        if number[3] == '0':
            raise ValueError("exchange code cannot start with zero")

        # if a phone number has an exchange code that starts with 1.
        if number[3] == '1':
            raise ValueError("exchange code cannot start with one")

        # if a phone number has an area code that starts with 0.
        if number[0] == '0':
            raise ValueError("area code cannot start with zero")

        # if a phone number has an area code that starts with 1.
        if number[0] == '1':
            raise ValueError("area code cannot start with one")

    def validate_quality(self, number):
        # if a phone number has less than 10 digits.
        if len(number) < 10:
            raise ValueError("incorrect number of digits")

        # if a phone number has more than 11 digits.
        if len(number) > 11:
            raise ValueError("more than 11 digits")

        # if a phone number has 11 digits, but starts with a number other than 1.
        if len(number) == 11:
            if number[0] == '1':
                number = number[1:]
            else:
                raise ValueError("11 digits must start with 1")

        # check for letters or punctuation
        if not number.isdigit():
            if any(c.isalpha() for c in number):
                raise ValueError("letters not permitted")
            else:   # not number or letter
                raise ValueError("punctuations not permitted")

        return number

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
