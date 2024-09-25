import os
from itertools import permutations
from arrays.MovingWindow import MovingWindow
from project_euler.utils.read_out_file import read_out_file

out_file = "permutations_0_to_9"


def write_zero_to_nine_permutations():
    permute_file_path = os.path.expanduser(
        f"~/scripts/py/src/project_euler/out/{out_file}.txt"
    )
    perms = ["".join([str(c) for c in t]) for t in permutations("0123456789")]
    print(perms)
    with open(permute_file_path, "a") as file:
        file.write(str(perms) + "\n")


# https://projecteuler.net/problem=43
class PandigitalSubstringAnalyzer:
    prime_divisors = [2, 3, 5, 7, 11, 13, 17]
    pandigits = read_out_file(out_file)
    pandigital = None

    def __init__(self):
        self.curr_window = MovingWindow(
            7, 10
        )  # delimiters of substring we're observing
        self.idx = -1

    @property
    def curr_substr(self):
        return int(self.pandigital[self.curr_window.start : self.curr_window.end])

    @property
    def curr_prime_divisor(self):
        return self.prime_divisors[self.idx]

    def show_status(self):
        print(
            f"""
        window: {self.curr_window}
        substring: {self.curr_substr}
        divisor: {self.curr_prime_divisor}
        
        {self.curr_substr} % {self.curr_prime_divisor} = {self.curr_substr % self.curr_prime_divisor}

        """
        )

    def find_digits_with_incremental_prime_divisors(self):
        nums = []
        for num in self.pandigits:
            self.pandigital = num

            print(f"""\n\nchecking: {num}\n- - - - - - - - - -\n""")

            while self.curr_substr % self.curr_prime_divisor == 0:
                self.show_status()

                if self.curr_window.start == 1:
                    print(f"pure pandivision found: {self.pandigital}")
                    nums.append(self.pandigital)
                    break

                self.curr_window.decrement()
                self.idx -= 1

            self.__init__()

        return nums


analyzer = PandigitalSubstringAnalyzer()
print(analyzer.find_digits_with_incremental_prime_divisors())
