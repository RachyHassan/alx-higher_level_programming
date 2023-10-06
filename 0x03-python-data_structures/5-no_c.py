#!/usr/bin/python3
def no_c(my_string):
    make = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(make))
