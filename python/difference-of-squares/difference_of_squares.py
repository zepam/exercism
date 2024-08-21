def square_of_sum(number):
    return sum(range(1, number + 1)) ** 2

def sum_of_squares(number):
    total = 0
    for n in range(1, number + 1):
        total += n*n
    return total

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
