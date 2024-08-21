class Luhn:
    def __init__(self, card_num):
        self.card_number = card_num.replace(' ', '')    # remove blank spaces
        pass

    def valid(self):
        if len(self.card_number) < 2 or self.card_number.isdigit() == False:
            return False
        check = 0

        for n in range(int(len(self.card_number)) - 1, -1, -1):
            digit = int(self.card_number[n])
            if digit % 2 == 0:    # alternate numbers are doubled
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            check += digit
            
        return check % 10 == 0
