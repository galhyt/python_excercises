import random

ColorEnum = {
    1: 'red',
    2: 'green',
    3: 'yellow',
    4: 'blue'
}


class Ball:
    color: int
    digit: int

    def __init__(self, color, digit):
        self.color = color
        self.digit = digit

    def __repr__(self):
        return f"({ColorEnum[self.color]}, {self.digit})"

    def weight(self):
        return self.color * 10 + self.digit


def push_to_start(balls: list, start_index: int, end_index: int, sel):
    i = start_index
    j = end_index
    while i < j:
        while sel(balls[i]) and i < j:
            i += 1
        while not sel(balls[j]) and j > i:
            j -= 1
        if i < j:
            tmp = balls[j]
            balls[j] = balls[i]
            balls[i] = tmp

    return i if sel(balls[i]) else i-1


def sort_balls(balls: list):
    # sorted_arr = sorted(balls, key=lambda b: b.weight())
    sections_indexes = []
    start_indx = 0
    for c, ctxt in list(ColorEnum.items())[:-1]:
        last_indx = push_to_start(balls, start_indx, len(balls)-1, lambda b: b.color == c)
        sections_indexes.append((start_indx, last_indx))
        start_indx = last_indx + 1
        print(f"{ctxt}: {balls}")
    sections_indexes.append((last_indx+1, len(balls)-1))

    for s_index, l_index in sections_indexes:
        start_indx = s_index
        for n in range(9):
            last_indx = push_to_start(balls, start_indx, l_index, lambda b: b.digit == n)
            start_indx = last_indx + 1
            print(f"{n}: {balls}")

    return balls


def create_sack(balls_num: int):
    return [Ball(random.randint(1, 4), random.randint(0, 9)) for _ in range(balls_num)]


balls_arr = create_sack(1000)
print(balls_arr)
sort_balls(balls_arr)
