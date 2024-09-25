from project_euler.utils.sieve_of_eratosthenes import sieve_of_eratosthenes
from project_euler.utils.derive_differences import get_frequency_of_differences
from itertools import permutations
from pydash import chunk


# https://projecteuler.net/problem=49
def prime_permuations():
    relevant_primes = list(filter(lambda n: n > 1000, sieve_of_eratosthenes(10000)))

    prime_string_set = list(
        set(map(lambda prime: "".join(sorted(str(prime))), relevant_primes))
    )

    # Suboptimal; we don't need to generate permutations of each prime.
    # Rather, we can filter for those elements which have permutations in list
    as_prime_permutations = list(
        sorted(
            map(
                lambda s: chunk(
                    "".join(
                        sorted(
                            [
                                "".join(p)
                                for p in set(permutations(s))
                                if int("".join(p)) in relevant_primes
                            ]
                        )
                    ),
                    4,
                ),
                prime_string_set,
            )
        )
    )[: len(prime_string_set) // 2]

    permutation_sequence_of_three = filter(
        lambda _l2: len(_l2),
        map(
            lambda _list: list(
                filter(
                    lambda s: len(s) == 3, get_frequency_of_differences(_list).values()
                )
            ),
            as_prime_permutations,
        ),
    )

    concatenated = list(map(lambda _l: sorted(list(_l)), permutation_sequence_of_three))

    print(concatenated)


prime_permuations()
