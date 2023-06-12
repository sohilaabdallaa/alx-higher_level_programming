#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if sentence[0] is None:
        new_tuple = len(sentence), None
    else:
        new_tuple = len(sentence), sentence[0]
    return new_tuple
