from functools import reduce
import time

start_time = time.time()

# Get data from stdin
line1 = input().split(' ')
K = int(line1[0])
M = int(line1[1])
lists = []
num_list = []
for _ in range(K):
    line = input().split(' ')
    lists.append([int(i) for i in line])

max_sum = 0
i_list = K * [0]
i_list[K - 1] = -1

time_dict = {}


def calc_func_time(func):
    def inner(*args):
        start_time = time.time()
        res = func(*args) if len(args) > 0 else func()
        if not (func.__name__ in time_dict.keys()):
            time_dict[func.__name__] = 0
        time_dict[func.__name__] += time.time() - start_time
        return res

    return inner


@calc_func_time
def calc(num_list: list):
    return reduce(lambda y, x: y+x ** 2, num_list, 0) % M


# Check if all lists indexes at the end
@calc_func_time
def check_end_iteration():
    global i_list
    for i in range(K):
        if i_list[i] != len(lists[i]) - 1:
            return False
    return True


def log_iteration(func):
    def _inner():
        func()
        print(f"lists: {lists} num_list: {num_list} max_sum: {max_sum}")
        # print(f"i_list: {i_list}")

    return _inner


# @log_iteration
@calc_func_time
def iterate_i_list():
    global i_list
    i = K - 1
    while i_list[i] == len(lists[i]) - 1 and i >= 0:
        i -= 1
    if i == -1:
        return False

    i_list[i] += 1
    for j in range(i + 1, K):
        i_list[j] = 0
    return True


while not check_end_iteration():
    iterate_i_list()
    num_list: list


    @calc_func_time
    def create_num_list():
        global num_list
        num_list = [lists[i][i_list[i]] for i in range(K)]
    create_num_list()
    cur_sum = calc(num_list)

    @calc_func_time
    def calc_max_sum():
        global max_sum
        max_sum = max(max_sum, cur_sum)
    calc_max_sum()

print(max_sum)
total_time = time.time() - start_time
for name, val in time_dict.items():
    print(f"{name}: {'{:.0f}'.format((val/total_time)*100)}%")
# print(f"total time: {sum(time_dict.values())}")
# print(f"{K} {M}\n{lists}")
