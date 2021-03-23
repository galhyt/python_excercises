#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#


def getMaxArea(w, h, isVertical, distance):
    # Write your code here
    def key_func_decorator(factor):
        def key_func(a):
            return a[0]*factor + a[1]
        return key_func

    lines = list(zip(isVertical, distance))
    lines.sort(key=key_func_decorator(10*max(map(lambda x: x[1], lines))))
    verticals = [line[1] for line in lines if line[0]] + [w]
    horizentals = [line[1] for line in lines if not line[0]] + [h]
    verticals_len = []
    horizentals_len = []
    verticals_len.append(verticals[0])
    for i in range(1, len(verticals)):
        d = verticals[i]-verticals[i-1]
        verticals_len.append(d)
    horizentals_len.append(horizentals[0])
    for i in range(1, len(horizentals)):
        d = horizentals[i]-horizentals[i-1]
        horizentals_len.append(d)

    return max(verticals_len) * max(horizentals_len)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open("input1_largest_area.txt") as file:
        lines = file.readlines()
    w = int(lines[0].strip())

    h = int(lines[1].strip())

    isVertical_count = int(lines[2].strip())

    isVertical = []

    for i in range(3, 3+isVertical_count):
        isVertical_item = int(lines[i].strip()) != 0
        isVertical.append(isVertical_item)

    distance_count = int(lines[3+isVertical_count].strip())

    distance = []

    for i in range(4+isVertical_count, 4+isVertical_count+distance_count):
        distance_item = int(lines[i].strip())
        distance.append(distance_item)

    result = getMaxArea(w, h, isVertical, distance)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
