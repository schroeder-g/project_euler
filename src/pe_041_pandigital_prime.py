import ast
import os

from maths.is_prime import is_prime


def generate_pandigital_primes(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    perms = ast.literal_eval(content)

    i = 0

    while i < len(perms):
        curr = perms[i]
        if is_prime(int(curr)):
            yield curr
        i += 1


# Usage
permute_file_path = os.path.expanduser(
    "~/scripts/py/src/project_euler/out/permutations_1_to_9.txt"
)
permutation_generator = generate_pandigital_primes(permute_file_path)

prime_pans = set()
for n in permutation_generator:
    prime_pans.add(n)

print(max(prime_pans))
