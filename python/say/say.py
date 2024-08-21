def say(number):

    number_names = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }

    tens_names = {
        2: 'hundred',     # two zeros
        3: 'thousand',   # three zeros
        4: 'million',  # four zeros
        5: 'billion', # nine zeros
        6: 'trillion', # twelve zeros
        7: 'quadrillion', # fifteen zeros
    }

    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = [100, 1000, 1000000, 1000000000, 1000000000000]
    unit_names = ['hundred', 'thousand', 'million', 'billion', 'trillion']

    for unit, unit_name in zip(units, unit_names):
        if number < unit * 1000:
            quotient = number // unit
            remainder = number % unit
            if remainder == 0:
                return say(quotient) + ' ' + unit_name
            else:
                return say(quotient) + ' ' + unit_name + ' ' + say(remainder)
            
    # # if number is between 1 and 20, return the number name
    # if number < 20:
    #     return number_names[number]
    
    # if number < 100:
    #     tens = number // 10
    #     remainder = number % 10
    #     if remainder == 0:
    #         return number_names[tens * 10]
    #     else:
    #         return number_names[tens * 10] + '-' + number_names[remainder]
        
    # if number < 1000:
    #     hundreds = number // 100
    #     remainder = number % 100
    #     if remainder == 0:
    #         return number_names[hundreds] + ' ' + tens_names[2]
    #     else:
    #         return number_names[hundreds] + ' ' + tens_names[2] + ' ' + say(remainder)
        
    # if number < 1000000:
    #     thousands = number // 1000
    #     remainder = number % 1000
    #     if remainder == 0:
    #         return say(thousands) + ' ' + tens_names[3]
    #     else:
    #         return say(thousands) + ' ' + tens_names[3] + ' ' + say(remainder)
        
    # if number < 1000000000:
    #     millions = number // 1000000
    #     remainder = number % 1000000
    #     if remainder == 0:
    #         return say(millions) + ' ' + tens_names[4]
    #     else:
    #         return say(millions) + ' ' + tens_names[4] + ' ' + say(remainder)
        
    # if number < 1000000000000:
    #     billions = number // 1000000000
    #     remainder = number % 1000000000
    #     if remainder == 0:
    #         return say(billions) + ' ' + tens_names[5]
    #     else:
    #         return say(billions) + ' ' + tens_names[5] + ' ' + say(remainder)
        
    # if number < 1000000000000000:
    #     trillions = number // 1000000000000
    #     remainder = number % 1000000000000
    #     if remainder == 0:
    #         return say(trillions) + ' ' + tens_names[6]
    #     else:
    #         return say(trillions) + ' ' + tens_names[6] + ' ' + say(remainder)
        
    # if number < 1000000000000000000:
    #     quadrillions = number // 1000000000000000
    #     remainder = number % 1000000000000000
    #     if remainder == 0:
    #         return say(quadrillions) + ' ' + tens_names[7]
    #     else:
    #         return say(quadrillions) + ' ' + tens_names[7] + ' ' + say(remainder)