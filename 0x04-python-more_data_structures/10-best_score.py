#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not isinstance(a_dictionary, dict):
        return None
    if len(a_dictionary) == 0:
        return None
    maxi = -1
    for key, value in a_dictionary.items():
        if maxi < a_dictionary[key]:
            maxi = a_dictionary[key]
            maxkey = key
    return maxkey
