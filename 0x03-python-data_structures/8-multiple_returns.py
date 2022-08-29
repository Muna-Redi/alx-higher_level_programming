#!/usr/bin/python3

def multiple_returns(sentence):
    lenght = len(sentence)
    if lenght > 0:
        char = sentence[0]
    else:
        char = "None"
    my_tuple = (lenght, char)
    return (my_tuple)
