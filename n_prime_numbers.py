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


@log_calls
def get_n_first_primes(n):
    if n == 1:
        return [2]
    
    pre_primes = get_n_first_primes(n-1)
    candidate = pre_primes[-1] + 1
    while True:
        if all((candidate%p != 0 for p in pre_primes)):
            return pre_primes + [candidate]
        candidate += 1


get_n_first_primes(400)
