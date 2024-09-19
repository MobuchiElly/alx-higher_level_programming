#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set(not set(set_1 & set_2))
