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
    """
    if len(arr) < 2:
        return 0 if len(arr) == 0 else max(0, max(arr))

    max_dict = [None]*len(arr)
    max_dict[0] = max(0, arr[0])
    max_dict[1] = max(max_dict[0], arr[1])
    for i in range(2, len(arr)):
        max_dict[i] = max(max_dict[i-1], max_dict[i-2]+arr[i])

    return max_dict[-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
