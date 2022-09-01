#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = 0
    if (not a_dictionary):
        return None
    for key, value in a_dictionary.items():
        if (value):
            if best_score <= value:
                best_score = value
                best = key
        else:
            return None
    return best
