def value(colors):
    COLOR_DICTIONARY =    {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
                'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    
    # method 1 using direct assignment of colors
    result = str(COLOR_DICTIONARY[colors[0]]) + str(COLOR_DICTIONARY[colors[1]])
    return int(result)
    """
    # method 2 using a for loop
    for word in colors:
        answer.append(str(COLOR_DICTIONARY.get(word)))
        if len(answer) == 2:
            return int("".join(answer))
    """

