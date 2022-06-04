#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    value = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            value.append(True)
        else:
            value.append(False)
    return (value)
