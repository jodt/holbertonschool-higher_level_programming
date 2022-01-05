#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum = 0
        diviseur = 0
        for tuple in my_list:
            sum += (tuple[0] * tuple[1])
            diviseur += tuple[1]
        return (sum/diviseur)
    else:
        return 0
