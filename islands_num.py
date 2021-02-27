import numpy as np
import itertools


def fill_ones_dict(nparr: np.ndarray, ones_dict: {tuple, bool}):
    for indices in zip(*np.where(nparr == 1)):
        ones_dict.update({tuple(indices): True})


def strike_out_ones(ones_dict: {tuple, bool}, arr_shape: ()):
    for indices in ones_dict.keys():
        if 0 in indices or indices[0] == arr_shape[0]-1 or indices[1] == arr_shape[1]-1:
            ones_dict[indices] = False
    
    for indices in filter(lambda ind: 0 < ind[0] < arr_shape[0] and 0 < ind[1] < arr_shape[1], ones_dict.keys()):
        for i_j in itertools.product(range(indices[0]-1, indices[0]+2), range(indices[1]-1, indices[1]+2)):
            if i_j in ones_dict.keys() and not ones_dict[i_j]:
                ones_dict[indices]= False
        

def islands_num(arr: list):
    """
    >>> islands_num([[0,0,0,0,0,0,0],
    ... [0,1,0,0,0,0,0],
    ... [0,0,1,0,0,0,0],
    ... [0,0,0,0,0,0,0],
    ... [0,1,1,0,0,0,0],
    ... [0,0,0,0,0,0,0]])
    2
    >>> islands_num([[1,0,0,0,0,0,0],
    ... [0,1,0,0,0,0,0],
    ... [0,0,1,0,1,0,0],
    ... [0,0,0,0,1,1,0],
    ... [0,1,1,1,0,0,0],
    ... [0,0,0,0,0,0,0]])
    1
    """
    nparr = np.array(arr)
    ones_dict: {tuple, bool} = {}

    if len(nparr.shape) == 1:
        return 0

    fill_ones_dict(nparr, ones_dict)
    strike_out_ones(ones_dict, nparr.shape)
    
    indx_dict = {indices: 1 for indices, free in ones_dict.items() if free}
    num = 0
    # iterate dict and remove current if linked to other ones. If not add 1 to number of islands and remove current

    def __inner_iterate__(indices):
        next_indices = []
        for i_j in itertools.product(range(indices[0]-1, indices[0]+2), range(indices[1]-1, indices[1]+2)):
            if i_j == indices:
                continue
            if i_j in indx_dict.keys():
                next_indices.append(i_j)
        del indx_dict[indices]
        if len(next_indices) > 0:
            for next_indx in next_indices:
                if next_indx in indx_dict.keys():
                    __inner_iterate__(next_indx)

    indices = next(iter(indx_dict.keys()), None)
    while indices:
        __inner_iterate__(indices)
        indices = next(iter(indx_dict.keys()), None)
        num += 1

    return num
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)