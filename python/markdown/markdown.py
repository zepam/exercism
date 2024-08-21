import re
# thanks to Limit91 for such a great example

def parse(markdown):
    result = []     # list

    
    for line in markdown.split('\n'):   # check each line, split by newline \n
        ## check for italics(em) and bold(strong)
        # for each mark '__' or '_', create a tag that says strong or em
        for mark, tag in {'__': 'strong', '_': 'em'}.items():
            #look for the pattern matching the markdown and sub the mark for the tag in line
            line = re.sub(pattern=f'(.*){mark}(.*){mark}(.*)', repl=fr'\1<{tag}>\2</{tag}>\3', string=line)

        ## check for headers
        # look for between 1 and 6 # in line
        if (m := re.match('(#{1,6}) (.*)', line)) is not None:
            # count the #s (h_count) that appear and use that count to create the <h#>
            length = len(m.group(1))
            # create a line <h#> [line starting from char after last #]</h#>/
            result.append(f'<h{(h_count := len(m.group(1)))}>{line[1 + h_count:]}</h{h_count}>')
        # now start looking for lists noted by *
        # assumption that list items don't include headers
        elif re.match(r'\* (.*)', line) is not None:    # found a #
            if len(result) == 0 or result[-1] != '</ul>': # if no closing </ul>
                result.append('<ul>')
            else:
                result.pop() # remove </ul> from end of result to add another item
            # add the line w/o the leading to chars '* '
            result.append(f'<li>{line[2:]}</li>')
            # now append the final </ul>
            result.append('</ul>') 
        else:
            # no list, so surround the line ith <p></p>
            result.append(f'<p>{line}</p>')
    # put the result[] and return as a string. '' means no separator character
    return ''.join(result)

    """
    lines = markdown.split('\n')
    res = ''
    in_list = False
    #in_list_append = False
    for i in lines:
        i = cleanHeaders(i)
        i = makeBold(i)
        i = makeItalic(i)

        #in_list, i = makeLists(in_list, i)
        i = makeLists(i)        # track in_list through the function to manage last bit
        i = makeParagraph(i)

        res += i

    if in_list:
        res += '</ul>'
    return res

def makeLists(i):
    in_list_append = False
    in_list = False
    # check for lists with a *
    m = re.match(r'\* (.*)', i)
        # \*(.*) => \* match a *, (anything 0 or more times)
    if m:
        current_line = m.group(1)
        if not in_list:
            in_list = True
            i = '<ul><li>' + current_line + '</li>'
        else:
            i = '<li>' + current_line + '</li>'
    else:
        if in_list:
            in_list_append = True
            in_list = False

    #i = makeParagraph(i)

    if in_list_append:
        i = '</ul>' + i
        in_list_append = False
    return i

def makeParagraph(current_line):
    m = re.match('<h|<ul|<p|<li', current_line)
    if not m:
        current_line = '<p>' + current_line + '</p>'
    return current_line

def makeItalic(current_line):
    m = re.match('(.*)_(.*)_(.*)', current_line)
    if m:
        current_line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return current_line

def makeBold(current_line):
    m = re.match('(.*)__(.*)__(.*)', current_line)
    if m:
        current_line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return current_line

def cleanHeaders(i):
    count_hash = len(i) - len(i.lstrip('#')) #count # at front of line
    if count_hash > 0 and count_hash < 7:   # limit headers from 1 - 7
        i = f'<h{count_hash}>{i[(count_hash+1):]}</h{count_hash}>'
    return i


    cleanup:
    remove is_bold and is_italic flags: were not used
    use i instead of curr

    move text changes to separate functions
    cleanHeaders: use number of # to format the line instead of multiple
                    if statements


"""