import ast
from multiprocessing.sharedctypes import Value

def answer(question):
   
    # doesn't start with what is
    if not question.startswith('What is'):
        raise ValueError('unknown operation')

    # starts with what is, but nothing comes after it
    if not bool(question[8:-1].strip().lower().split()):
        raise ValueError('syntax error')

    words = question.lower()
    words = words.replace('what is ', '').replace('?', '')
    words = words.replace('plus', '+').replace('minus', '-').replace('multiplied by', '*').replace('divided by', '/')
    word_list = words.split(" ")
    words = words.replace(" ", "")

    if len(word_list) < 3 or not check_structure(word_list):
        if words.isdigit():
            return int(words)
        elif word_list[-1].isalpha():
            raise ValueError("unknown operation")
        elif not check_structure(word_list):
            raise ValueError("syntax error")
        raise ValueError("unknown operation")

    if len(word_list) > 3:
        big_words = list()
        for w in word_list:
            big_words.append(w)
            if len(big_words) == 3:
                try:
                    eval(''.join(big_words))
                    answer = eval(''.join(big_words))
                    big_words.clear()
                    big_words.append(str(answer))
                except:
                    raise ValueError("syntax error")             
    else:
        answer = eval(words)
    return answer

def check_structure(word_list):
    correct = True
    for n in range(len(word_list)):
        check = word_list[n].replace('-', '')
        if n%2 == 0:
            if check.isdigit() is False:
                correct = False
        if n%2 == 1:
            if check.isdigit() is True:
                correct = False
    if not check.isnumeric():
        correct = False 
    return correct

