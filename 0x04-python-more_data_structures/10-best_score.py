#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    res = ""
    if a_dictionary:
        for k, l in a_dictionary.items():
            if l > i:
                res = k
                i = l
        return res
    else:
        return(None)
