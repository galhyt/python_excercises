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

Output:
0
2

Explanation:
Testcase 2: There are 2 possible paths with exactly K coins, which are (1 + 4 + 3 + 2 + 1) and (1 + 2 + 3 + 5 + 1).

"""
import numpy as np


class TestCase:
    X: int
    matrix: np.ndarray

    def __init__(self, X: int, matrix: np.ndarray):
        self.X = X
        self.matrix = matrix

    def __repr__(self):
        return f"X coins: {self.X} matrix: {self.matrix}"

    @staticmethod
    def get_ndarray_from_str(N: int, line: str):
        arr = list(map(int, line.split(' ')))
        return np.array_split(ary=arr, indices_or_sections=N)

    def get_paths(self) -> [tuple]:
        pass

    def _get_path(self, start: tuple) -> tuple:
        pass


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        X = int(input())
        N = int(input())
        test_case = TestCase(X, TestCase.get_ndarray_from_str(N, input()))
        paths = test_case.get_paths()
        # print paths of t test case


