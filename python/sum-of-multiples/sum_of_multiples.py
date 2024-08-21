def sum_of_multiples(limit, multiples):
    ## this method cycles through each number up to limit and checks if it
    ## is a factor
    #sum_of_multi = set()    # a set keeps out duplicates
    # for n in range(1, limit):
    #     for x in range(1, len(multiples)+1):
    #         if multiples[x-1] != 0:
    #             if n%multiples[x-1] == 0:
    #                 sum_of_multi.add(n)
    # return sum(list(sum_of_multi))

    ## this method counts up by the factors and doesn't have to do the factor
    ## check. Because of course a factor qualifies.
    sum_of_multi = set()
    for n in multiples:
        if n is not 0:
            for multi in range(n, limit, n):
                sum_of_multi.add(multi)
    return sum(sum_of_multi)

