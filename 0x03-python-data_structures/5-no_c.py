#!/usr/bin/python3

def no_c(my_string):
    up = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            up += i
    return (up)