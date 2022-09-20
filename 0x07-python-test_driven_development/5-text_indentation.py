#!/usr/bin/python3

def text_indentation(text):
    """ This function prints a text with 2 lines after any of the charracters
    '.', '?', ':'
    args:
        text (str): text to be printed

    return:
        returns nothing

    raises:
        TypeError: text must be a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        print(text[i], end='')

        if text[i] in ['.', '?', ':']:
            print('\n')

