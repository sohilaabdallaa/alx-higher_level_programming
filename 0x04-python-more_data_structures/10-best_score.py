#!/usr/bin/python3
def best_score(a_dictionary):
    maxi = 0
    if a_dictionary is None:
        return None
    for key, value in a_dictionary.items():
        if maxi < a_dictionary[key]:
            maxi = a_dictionary[key]
            maxkey = key
    return maxkey
