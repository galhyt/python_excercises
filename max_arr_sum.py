import numpy as np
import itertools


# def get_max_arr_sum(arr: [int]):
#     """
#     >>> get_max_arr_sum([1,2,3,4,5])
#     9
#     >>> get_max_arr_sum([-2,1,3,-4,5])
#     8
#     >>> get_max_arr_sum([3, 5, -7, 8, 10])
#     15
#     """
#     def __get_max__(np_arr: np.ndarray):
#         max_val = 0
#         for ln in range(1, len(np_arr)+1):
#             print(list(itertools.combinations(np_arr, ln)))
#             max_val = max(max_val, max((sum(comb) for comb in itertools.combinations(np_arr, ln))))
#         return max_val
#
#     np_arr: np.ndarray = np.array(arr)
#     return max(__get_max__(np_arr[::2]), __get_max__(np_arr[1::2]))


def get_max_arr_sum(arr):
    """
    >>> get_max_arr_sum([1,2,3,4,5])
    9
    >>> get_max_arr_sum([-2,1,3,-4,5])
    8
    >>> get_max_arr_sum([3, 5, -7, 8, 10])
    15
    """
    def peek_combination(i):
        yield [arr[i]]
        for j in range(i+2, len(arr)):
            for comb in peek_combination(j):
                yield [arr[i]] + comb

    max_val = 0
    for i in range(len(arr)):
        for comb in peek_combination(i):
            max_val = max(max_val, sum(comb))

    return max_val


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)