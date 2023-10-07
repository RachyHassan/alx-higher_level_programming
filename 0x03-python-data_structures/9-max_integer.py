#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for v in range(len(my_list)):
        if my_list[v] > big:
            big = my_list[v]

        return (big)
