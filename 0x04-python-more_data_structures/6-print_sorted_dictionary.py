#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
  res_keys = sorted(a_dictionary.keys())
  for key in res_keys:
    print(f"{key}: {a_dictionary[key]}")
