#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    result = 0
    for i in range(0, list_length):
        try:
            result = my_list[i] / my_list[i]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        except TypeError:
            result = 0
            print("wrong type")
    finally:
        pass
        result_list.append(result)
    return result_list
