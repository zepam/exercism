def slices(series, length):
    ## DATA VALIDATION SECTION
    # if the slice length is zero.
    if length == 0:
        raise ValueError("slice length cannot be zero")
    # if the slice length is negative.
    if length < 0:
        raise ValueError("slice length cannot be negative")
    # if the series provided is empty.
    if len(series) == 0:
        raise ValueError("series cannot be empty")
    # if the slice length is longer than the series.
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    results = []

    for i in range(len(series) - length + 1):
        results.append(series[0 + i:length + i])

    return results