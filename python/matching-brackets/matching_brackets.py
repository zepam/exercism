from collections import deque

SYMBOLS = {'[':']', '{':'}', '(':')'}

def is_paired(input_string):
    # create a stack
    symbol_stack = deque()
    # check the symbol in input_string
    for i in input_string:
        # skips over chars not being checked
        if i in SYMBOLS.keys():        
            symbol_stack.append(i)
        elif i in SYMBOLS.values():
            if not symbol_stack:
                return False
            peek = symbol_stack.pop()  
            if i is not SYMBOLS[peek]:
                return False
    # return true if stack is empty at the end
    return len(symbol_stack) == 0
