#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_del = []
    for k, v in a_dictionary.items():
        if a_dictionary[k] == value:
            keys_to_del.append(k)
    for key in keys_to_del:
        a_dictionary.pop(key)
    return a_dictionary
