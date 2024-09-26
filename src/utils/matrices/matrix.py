import numpy as np


class Matrix:
    def __init__(self, grid):
        self.grid: [[]] = grid

    def get_horizontal_values(self, x, y, length):
        if x + length > len(self.grid[x]):
            return None
        return self.grid[y][x : x + length]

    def get_vertical_values(self, x, y, length):
        if y + length > len(self.grid):
            return None
        return [self.grid[i][x] for i in range(y, y + length)]

    def get_diagonal_up_values(self, x, y, length):
        if x + length > len(self.grid[0]) or y - length < 0:
            return None

        ans = []
        for i in range(length):
            ans.append(self.grid[y - i][x + i])
        return ans

    def get_diagonal_down_values(self, x, y, length):
        if x + length > len(self.grid[0]) or y + length > len(self.grid):
            return None

        ans = []
        for i in range(length):
            ans.append(self.grid[y + i][x + i])

        return ans

    def are_horizonally_aligned(self, xy1, xy2):
        pass

    @staticmethod
    def get_largest_grid_product(self, length):
        max_ = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                horiz = get_horizontal_values(matrix, i, j, length)
                if horiz and prod(horiz) > max_:
                    max_ = prod(horiz)

                vert = get_vertical_values(matrix, i, j, length)
                if vert and prod(vert) > max_:
                    max_ = prod(vert)

                diag_up = get_diagonal_up_values(matrix, i, j, length)
                if diag_up and prod(diag_up) > max_:
                    max_ = prod(diag_up)

                diag_down = get_diagonal_down_values(matrix, i, j, length)
                if diag_down and prod(diag_down) > max_:
                    max_ = prod(diag_down)

        return max_
