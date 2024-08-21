def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    def find_factors(number):
        factors = [1]
        for n in range(2, number):
            if number % n == 0:
                factors.append(n)
        if len(factors) == 1:   # catch if number is 1
            return 0
        return sum(factors)

    aliquot_sum = find_factors(number)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"

    return "deficient"
    #return (number == find_factors(number))
