def transform(legacy_data):
    results = dict()
    for k, v in legacy_data.items():
        for c in v:
            letter = c.lower()
            results[letter] = k
    return results
