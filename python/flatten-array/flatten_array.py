def flatten(iterable):
    results = []
    for i in iterable:
        if isinstance(i, list):
            results.extend(flatten(i)) #recursion!
        elif isinstance(i, int):
            results.append(i)
    return results
