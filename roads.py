#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numberOfWays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY roads as parameter.
#
# returns the number of ways to put 3 hotels in three different cities while the distance between the hotels is equal

def numberOfWays(roads):
    # Write your code here
    print(roads)
    dist_dict = {}

    def set_dist_dict(new_key, key):
        dist_dict[new_key] = dist_dict[key] + 1 if new_key not in dist_dict.keys() else min(dist_dict[new_key],
                                                                                            dist_dict[key] + 1)

    def check_key(r):
        keys = [(min(key), max(key)) for key in dist_dict.keys()]
        new_keys = []
        for key in keys:
            if r[0] not in key and r[1] not in key: continue
            if r[0] == key[1]:
                if key[0] != r[1]:
                    new_key = (min(key[0], r[1]), max(key[0], r[1]))
                    set_dist_dict(new_key, key)
                    new_keys.append(new_key)
            if r[0] == key[0]:
                if key[1] != r[1]:
                    new_key = (min([key[1], r[1]]), max([key[1], r[1]]))
                    set_dist_dict(new_key, key)
                    new_keys.append(new_key)
            if r[1] == key[0]:
                if r[0] != key[1]:
                    new_key = (min([r[0], key[1]]), max([r[0], key[1]]))
                    set_dist_dict(new_key, key)
                    new_keys.append(new_key)
            if r[1] == key[1]:
                if r[0] != key[0]:
                    new_key = (min([r[0], key[0]]), max([r[0], key[0]]))
                    set_dist_dict(new_key, key)
                    new_keys.append(new_key)
        return new_keys

    for _ in range(len(roads)):
        for r in map(lambda x: (min(x), max(x)), roads):
            dist_dict[r] = 1
            check_key(r)

    print(dist_dict)

    def distance(a, b):
        return dist_dict[(a,b)]

    ret = 0
    n = len(roads)+1
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1, n+1):
                dist_ij = distance(i, j)
                if dist_ij == distance(i, k) and dist_ij == distance(j, k):
                    ret += 1
    return ret


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open("input1_roads.txt") as file:
        lines = file.readlines()
        roads_rows = int(lines[0].strip())
        roads_columns = int(lines[1].strip())

        roads = []

        for i in range(2, len(lines)):
            roads.append(list(map(int, lines[i].rstrip().split())))

    result = numberOfWays(roads)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
