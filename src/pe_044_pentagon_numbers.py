from utils.timer import timer

# https://projecteuler.net/problem=44


class PentagonalNumberStream:
    def __init__(self):
        self.stream = set()
        self.stream_order = []

    def generate_pentagonal_numbers(self):
        n = 2
        while True:
            num = n * (3 * n - 1) / 2
            self.stream_order.append(num)
            self.stream.add(num)
            yield num
            n += 1

    def is_pentagonal_number(self, n):
        return True if n in self.stream else False

    @timer
    def find_pent_pairs_with_pentagonal_sum_and_diff(self):
        gen = self.generate_pentagonal_numbers()
        big_index = 0
        while True:
            while len(self.stream_order) <= big_index:
                next(gen)
            big = self.stream_order[big_index]

            for little in self.stream_order[:big_index][::-1]:
                pent_diff = big - little
                if self.is_pentagonal_number(pent_diff):
                    pent_sum = big + little
                    # Generate pentagonal numbers up to pent_sum if needed
                    while self.stream_order[-1] < pent_sum:
                        next(gen)
                    if self.is_pentagonal_number(pent_sum):
                        return pent_diff
            big_index += 1


print(PentagonalNumberStream().find_pent_pairs_with_pentagonal_sum_and_diff())
