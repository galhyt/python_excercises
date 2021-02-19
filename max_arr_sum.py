import numpy as np
import itertools
from threading import Timer


def get_max_arr_sum(arr):
    """
    >>> get_max_arr_sum([1,2,3,4,5])
    9
    >>> get_max_arr_sum([-2,1,3,-4,5])
    8
    >>> get_max_arr_sum([3, 5, -7, 8, 10])
    15
    >>> with open('input1_max_arr_sum.txt', 'r') as file:
    ...     txt = file.read()
    ...     get_max_arr_sum(list(map(int, txt.split(' '))))
    151598486
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    """
    max_dict = [None]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        print('\r', i, end='')
        i_max_val = arr[i]
        if i+2 < len(arr):
            i_max_val = max(i_max_val, arr[i] + max(max_dict[i+2:]))

        max_dict[i] = i_max_val

    return max(max_dict)


if __name__ == '__main__':
    import doctest
    with open('input1_max_arr_sum.txt', 'r') as file:
        txt = file.read()
        get_max_arr_sum(list(map(int, txt.split(' '))))
    # doctest.testmod(verbose=True)