#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if i == "":
            return None
        else:
            return (len(sentence), sentence[0])
