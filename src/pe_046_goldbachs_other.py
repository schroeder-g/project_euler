from project_euler.utils.sieve_of_eratosthenes import gen_primes as generate_primes
from project_euler.utils.is_prime import is_prime


# https://projecteuler.net/problem=46
class FindTheOddCompositeException:
    def __init__(self):
        self.odd_composite_sums = set()

    def gen_double_squares(self):
        n = 1

        while True:
            yield n**2 * 2
            n += 1

    def gen_composite_odds(self):
        odd = 9
        yield odd

        while True:
            odd += 2

            if not is_prime(odd):
                yield odd
            else:
                continue

    def generate_prime_and_odd_sums(self):
        primes_gen = generate_primes()
        primes = [next(primes_gen)]
        primes_indices = [0]  # Indices for squares

        squares_gen = self.gen_double_squares()
        squares = [next(squares_gen)]
        squares_indices = [0]  # Indices for squares

        heap = []
        visited = set()

        # Initialize the heap with the first sum
        initial_sum = primes[0] + squares[0]
        hq.heappush(heap, (initial_sum, 0, 0))  # (sum, prime_index, square_index)
        visited.add((0, 0))

        while heap:
            s, i_p, i_s = hq.heappop(heap)

            if not (len(heap) and heap[0][0] == s):
                yield s

            # Generate the next prime if needed
            i_p_next = i_p + 1
            if i_p_next == len(primes):
                next_prime = next(primes_gen)
                primes.append(next_prime)
                primes_indices.append(i_p + 1)

            if (i_p_next, i_s) not in visited:
                visited.add((i_p_next, i_s))
                _sum = primes[i_p_next] + squares[i_s]
                hq.heappush(heap, (_sum, i_p_next, i_s))

            # Generate the next square if needed
            i_s_next = i_s + 1
            if i_s_next == len(squares):
                next_square = next(squares_gen)
                squares.append(next_square)
                squares_indices.append(i_s + 1)

            if (i_p, i_s_next) not in visited:
                visited.add((i_p, i_s_next))
                _sum = primes[i_p] + squares[i_s_next]
                hq.heappush(heap, (_sum, i_p, i_s_next))

    def find_odd_composite_exception(self):
        g_sums = self.generate_prime_and_odd_sums()
        next(g_sums)
        next(g_sums)
        next(g_sums)
        sum_ = next(g_sums)

        generate_odd_composite = self.gen_composite_odds()
        curr_composite = next(generate_odd_composite)

        while True:
            if curr_composite == sum_:
                curr_composite = next(generate_odd_composite)
                while sum_ < curr_composite:
                    sum_ = next(g_sums)
                continue

            yield curr_composite


g = FindTheOddCompositeException().find_odd_composite_exception()

for i in range(1, 10000):
    print(next(g))
