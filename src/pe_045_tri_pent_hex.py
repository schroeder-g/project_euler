from maths.quadratic_formula import quad
from utils.timer import timer


# https://projecteuler.net/problem=45
class TPHFinder:
    @staticmethod
    def gen_hexagonal_numbers():

        n = 144  # First instance of a tri/pent/hex number is 143 in hex series
        while True:
            computed = n * (2 * n - 1)

            n += 1

            yield computed

    @staticmethod
    def is_triangular_number(value: int):
        # Triangle(n) = n(n + 1) / 2

        solution = quad(1, -1, -value * 2)[0]
        return int(solution) == solution

    @staticmethod
    def is_pentagonal_number(value: int):
        # Pentagon(n) = n(3n - 1) / 2

        solution = quad(3, -1, -value * 2)[0]
        return int(solution) == solution

    @timer
    @staticmethod
    def find_next_solution():

        gen = TPHFinder.gen_hexagonal_numbers()

        for num in gen:
            if TPHFinder.is_pentagonal_number(num) and TPHFinder.is_triangular_number(
                num
            ):
                return num


print(TPHFinder.find_next_solution())
