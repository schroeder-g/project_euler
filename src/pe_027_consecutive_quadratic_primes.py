from maths.sieve_of_eratosthenes import sieve_of_eratosthenes


def get_most_primal_coefficients():
    primes = sieve_of_eratosthenes(100000000)

    max_primes_list = []
    maximal_coefficients: tuple = ()

    for a in range(-1000, 1000):
        for b in range(-1000, 1001):
            n = 0
            local_primes = []
            while True:
                product = produce_quadratic_output(n, a, b)
                if product in primes:
                    local_primes.append(product)
                    if len(local_primes) > len(max_primes_list):
                        print(f"New Greatest Consecutive list found! {local_primes}")
                        max_primes_list = local_primes
                        maximal_coefficients = (a, b)
                    n += 1
                else:
                    break
    return maximal_coefficients[0] * maximal_coefficients[1]


def produce_quadratic_output(n, a, b):
    return (n**2) + (a * n) + b
