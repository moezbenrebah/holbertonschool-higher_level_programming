#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    if type(obj) is a_class:
        return True
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
