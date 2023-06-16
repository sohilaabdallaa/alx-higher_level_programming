#!/usr/bin/python3
def weight_average(my_list=[]):
    division = 0
    av_weigth = 0
    if not my_list:
        return 0
    for i in my_list:
        av_weigth += i[0] * i[1]
        division += i[1]
    return float(av_weigth/division)
