import pprint
import time

iteration_no = [0]


def log_calls(func):
    def inner(n):
        res = func(n)
        if n >= 2:
            candiates_no = res[-1]-res[-2]
            iteration_no.append(candiates_no*(n-1)+iteration_no[-1])
            print(f"{func.__name__}({n})\t:{iteration_no[-1]}\t{n**2}")
        return res
    return inner


recurse_dict = {}
def recurse_emulation(func):
    def inner(n):
        if func.__name__ not in recurse_dict:
            recurse_dict.update({func.__name__: []})
        results_arr = recurse_dict[func.__name__]
        if len(results_arr) >= n:
            return results_arr[:n]
        else:
            m = len(results_arr) + 1
            while m <= n:
                results_arr = recurse_dict[func.__name__] = func(m)
                m += 1
            return results_arr
    return inner

@recurse_emulation
def get_n_first_primes(n):
    if n == 1:
        return [2]
    
    pre_primes = get_n_first_primes(n-1)
    candidate = pre_primes[-1] + 1
    while True:
        if all((candidate%p != 0 for p in pre_primes)):
            return pre_primes + [candidate]
        candidate += 1


pprint.pprint(get_n_first_primes(4000))
