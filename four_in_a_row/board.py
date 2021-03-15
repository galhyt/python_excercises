import numpy as np


class Board(np.ndarray):
    class Disks:
        yellow = 0
        red = 1

    def __new__(cls):
        return np.asarray([[None]*7]*6).view(cls)

    def __str__(self):
        return '\n'.join(('|'.join(map(lambda x: 'O' if x == Board.Disks.red else 'x' if x == Board.Disks.yellow
        else ' ', row)) for row in self))

    def insert(self, col, color):
        empty_indices = np.where(self[:, col] == None)
        if len(empty_indices) == 0: return False
        row = max(*empty_indices)
        self[row, col] = color
        return True

    def is_a_winner(self):
        if self.__is_a_winner__(Board.Disks.red): return Board.Disks.red
        if self.__is_a_winner__(Board.Disks.yellow): return Board.Disks.yellow
        return None

    def __is_a_winner__(self, color):
        coordinates: (np.ndarray, np.ndarray) = np.where(self == color)
        rows, cols = coordinates[0], coordinates[1]
        coordinates = zip(*coordinates)
        # if len(coordinates) < 4: return False

        # check rows
        for i in range(6):
            r_indxs = np.where(rows == i)[0]
            if len(r_indxs) >= 4:
                count = 1
                for j in range(1, len(r_indxs)):
                    if cols[r_indxs[j]] != cols[r_indxs[j-1]]+1:
                        count = 1
                    else:
                        count += 1
                if count >= 4: return True
        # check columns
        for i in range(7):
            c_indxs = np.where(cols == i)[0]
            if len(c_indxs) >= 4:
                count = 1
                for j in range(1, len(c_indxs)):
                    if rows[c_indxs[j]] != rows[c_indxs[j-1]]+1:
                        count = 1
                    else:
                        count += 1
                if count >= 4: return True
        # check diagonals
        def is_in_diagonal(coor, r_fac, c_fac):
            next_coor = (coor[0]+r_fac, coor[1]+c_fac)
            if next_coor[0] < 0 or next_coor[0] > 5 or next_coor[1] < 0 or next_coor[1] > 6:
                return 1
            if next_coor in coordinates:
                return is_in_diagonal(next_coor, r_fac, c_fac) + 1
            return 1

        for coor in coordinates:
            if is_in_diagonal(coor, -1, 1) >= 4: return True
            if is_in_diagonal(coor, 1, 1) >= 4: return True
            if is_in_diagonal(coor, 1, -1) >= 4: return True
            if is_in_diagonal(coor, -1, -1) >= 4: return True
        return False

