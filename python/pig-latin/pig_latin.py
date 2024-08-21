import re

# compile the expression into a pattern object
CONSONANTS = re.compile(r"""^(          # look at the front of the word
                        [^aeiou]?qu     # Rule 3 - look for 0 or 1 consonant followed by qu                        
                        |               # rule 3 has to check before rule 2
                        [^aeiouy]+      # Rule 2 - consonant start
                        |               # 
                        y(?=[aeiou])    # Rule 4 - y followed by a vowel
                        )([a-z]*        # the rest of the letters in the word
                        )""", re.VERBOSE)
VOWELS = re.compile(r"""^(
                        [aeiou]|        # starts with a vowel
                        xr|             # starts with x
                        y[^aeiou])      # starts with y then a consonant
                        [a-z]*          # the rest of the word
                        """, re.VERBOSE)    


def vowel_check(text):
    return VOWELS.match(text) is not None

def consonant_split(text):
    return CONSONANTS.match(text).groups()

def translate(text):
    words = []
    for word in text.split():
        if vowel_check(word):
            word = word + 'ay'
        else:
            head, tail = consonant_split(word)
            word = tail + head + 'ay'
        words.append(word)
    return ' '.join(words)
