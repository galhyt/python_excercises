"""
Given a N x N matrix where every cell has some number of coins. Count number of ways to reach bottom right cell
of matrix from top left cell with exactly K coins. We can move to (i+1, j) or (i, j+1) from a cell (i, j).

Input:
First line contains number of test cases T. For each test case, first line contains the integer value 'X'
denoting coins, second line contains an integer 'N' denoting the order of square matrix. Last line contains N x N
elements in a single line in row-major order.

Output:
Output the number of paths possible.

Constraints:
1 <=T<= 500
1 <= K <= 200
1 <= N <= 200
1 <= Ai <= 200

Example:
Input:
2
16
3
1 2 3 4 6 5 9 8 7
12
3
1 2 3 4 6 5 3 2 1

1 2 3
4 6 5
3 2 1

Output:
0
2

Explanation:
Testcase 2: There are 2 possible paths with exactly K coins, which are (1 + 4 + 3 + 2 + 1) and (1 + 2 + 3 + 5 + 1).

"""
import numpy as np
from typing import Tuple


class TestCase:
    X: int
    N: int
    last_index: int
    matrix: np.ndarray

    def __init__(self, X: int, N: int, matrix: np.ndarray):
        self.X = X
        self.N = N
        self.matrix = matrix
        self.last_index = N - 1

    def __repr__(self):
        return f"X coins: {self.X} matrix: {self.matrix}"

    @staticmethod
    def get_ndarray_from_str(N: int, line: str):
        arr = list(map(int, line.split(' ')))
        return np.array(np.array_split(ary=arr, indices_or_sections=N))

    def get_paths(self) -> [([Tuple[int]], [int])]:
        """
        :return: array of tuples of the form (path: created by coordinates, array consist of values of the path cells)
        """
        paths = self._get_paths()
        if paths is None:
            return None

        return [(path, [self.matrix[cell] for cell in path]) for path in paths]

    def _get_paths(self) -> [[Tuple[int]]]:
        def inner(start: Tuple[int], goal_sum: int) -> [[Tuple[int]]]:
            paths = []
            if self.matrix[start] > goal_sum:
                return None

            if start == (self.last_index, self.last_index):
                if self.matrix[start] == goal_sum:
                    return [[start]]
                else:
                    return None

            next_cell = []
            if start[1] < self.last_index:
                next_cell.append((start[0], start[1] + 1))
            if start[0] < self.last_index:
                next_cell.append((start[0] + 1, start[1]))

            for cell in next_cell:
                next_path = inner(cell, goal_sum - self.matrix[start])
                if next_path is not None:
                    for path in next_path:
                        paths.append([start] + path)

            return None if len(paths) == 0 else paths

        paths = inner((0, 0), self.X)
        return paths


def ordinal(n):
    return '1st' if n == 1 else '2nd' if n == 2 else '3rd' if n == 3 else f"{n}th"


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        X = int(input())
        N = int(input())
        test_case = TestCase(X, N, TestCase.get_ndarray_from_str(N, input()))
        paths = test_case.get_paths()
        print(f"paths of {ordinal(t)} test case: {'none' if paths is None else ''}")
        if paths is not None:
            for path in paths:
                print(f"\t{'+'.join(map(str, path[1]))}")
