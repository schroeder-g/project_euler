from project_euler.utils.sieve_of_eratosthenes import gen_primes
from project_euler.utils.is_prime import is_prime
from sets.powerset import powerset
from collections import defaultdict


def find_eight_prime_value_family():
    primes = gen_primes()

    toss_p = next(primes)
    while toss_p <= 56003:
        toss_p = next(primes)

    families = defaultdict(set)

    seen_p = set()
    for p in primes:
        if p in seen_p:
            continue

        base_p = str(p)
        for replacement_ids in powerset(range(len(base_p))):
            family_id = [*base_p]

            for char_i, char in enumerate(family_id[:-1]):
                if char_i in replacement_ids:
                    family_id[char_i] = "*"

            joined = "".join(family_id)
            for n in range(10):
                compiled = int(joined.replace("*", str(n)))
                if len(str(compiled)) == len(family_id) and is_prime(compiled):
                    print(compiled)
                    seen_p.add(compiled)
                    families[joined].add(compiled)

        if max([len(fam) for fam in families.values()]) >= 8:
            print(list(filter(lambda i: len(i[1]) > 6, families.items())))
            break

    print(min(sorted(families.values(), key=lambda f: len(f), reverse=True)[0]))


find_eight_prime_value_family()
