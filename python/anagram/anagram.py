def find_anagrams(word, candidates):
    results = []
    for w in candidates:
        if sorted(word.lower()) == sorted(w.lower()):
            if word.lower() != w.lower():
                results.append(w)
    return results
