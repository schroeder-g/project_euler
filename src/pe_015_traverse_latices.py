from maths.create_pascal_triangle import create_pascal_triangle
from typing import Any


class Matrix:
    def __init__(self, grid=[]):
        self.grid: [[Any]] = grid
        self.paths = self.trace_paths(
            start={"x": 0, "y": 0},
            end={"x": len(self.grid) - 1, "y": len(self.grid[0]) - 1},
            curr_el={"x": 0, "y": 0},
            paths=[],
            curr_path=[],
        )
        self.num_paths = len(self.paths)

    """ Viable paths when moving right and down"""

    def trace_paths(self, start, end, curr_el, paths, curr_path=None):
        c_pa = curr_path.copy()
        if not len(self.grid):
            raise Exception("Grid empty; no matrix to traverse")
        elif not start["x"] <= end["x"] or not start["y"] <= end["y"]:
            raise Exception("Start must be placed to the left of or above end")
        elif not 0 <= start["x"] < len(self.grid[-1]) or not 0 <= start["y"] < len(
            self.grid
        ):
            raise Exception("Start outside bounds of matrix")
        elif not 0 <= end["x"] < len(self.grid[-1]) or not 0 <= end["y"] < len(
            self.grid
        ):
            raise Exception("End outside bounds of matrix")

        if curr_el["x"] == end["x"]:
            for i in range(0, end["y"] - curr_el["y"] + 1):
                c_pa.append(
                    {
                        (curr_el["x"], curr_el["y"] + i): self.grid[curr_el["y"] + i][
                            curr_el["x"]
                        ]
                    }
                )
            return c_pa
        elif curr_el["y"] == end["y"]:
            for i in range(0, end["x"] - curr_el["x"] + 1):
                c_pa.append(
                    {
                        (curr_el["x"] + i, curr_el["y"]): self.grid[curr_el["y"]][
                            curr_el["x"] + i
                        ]
                    }
                )
            return c_pa

        c_pa.append(
            {(curr_el["x"], curr_el["y"]): self.grid[curr_el["y"]][curr_el["x"]]}
        )
        paths.append(
            self.trace_paths(
                start, end, {"x": curr_el["x"] + 1, "y": curr_el["y"]}, paths, c_pa
            )
        )
        paths.append(
            self.trace_paths(
                start, end, {"x": curr_el["x"], "y": curr_el["y"] + 1}, paths, c_pa
            )
        )
        return paths

    def __str__(self):
        return str(self.paths)


def get_binomial_expansion(n):
    tri = create_pascal_triangle((n + 1) * 2)
    products = tri[::2]
    return products[-1][n]
