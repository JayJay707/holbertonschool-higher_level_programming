#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return(None)
    k = my_list[0]
    for x in my_list:
        if x > k:
            k = x
    return(k)
