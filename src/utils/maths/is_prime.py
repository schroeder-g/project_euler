from maths.is_factor import is_factor


def defunct_is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True

    for div in range(abs(n))[2:]:
        if is_factor(n, div):
            return False
    return True


def is_prime(n):
    if n < 4:
        return False if n < 2 else True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
    return True


# def miller_rabin(n, k=5):
#     if n < 2:
#         return False
#     if n in (2, 3):
#         return True
#     if not n & 1:
#         return False

#     s, d = 0, n - 1
#     while d % 2 == 0:
#         s, d = s + 1, d >> 1

#     for _ in range(k):
#         a = random.randrange(2, n - 2)
#         x = pow(a, d, n)
#         if x == 1 or x == n - 1:
#             continue
#         for _ in range(s - 1):
#             x = pow(x, 2, n)
#             if x == n - 1:
#                 break
#         else:
#             return False
#     return True

# def jacobi(a, n):
#     assert(n > a > 0 and n % 2 == 1), f"{n} doesn't fit;\n {n} > {a} > 0 = {n > a > 0};\n {n} % 2 == 1 = {n % 2 == 1}"
#     s = 1
#     while a != 0:
#         while a % 2 == 0:
#             a //= 2
#             if n % 8 in (3, 5):
#                 s = -s
#         a, n = n, a
#         if a % 4 == 3 and n % 4 == 3:
#             s = -s
#         a %= n
#     return s if n == 1 else 0

# def lucas_probable_prime(n, D):
#     P = 1
#     Q = (1 - D) // 4

#     def mod_lucas_seq(n, P, Q, k):
#         u, v = 0, 2
#         u2m, v2m = 1, P
#         qm, qm2, qkd = Q, Q*Q, Q
#         for bit in reversed(bin(k)[2:]):
#             u2m, v2m = (u2m * v2m) % n, (v2m*v2m - 2*qm2) % n
#             qm2 = (qm2 * qm2) % n
#             if bit == '1':
#                 u, v = (u2m * v + u * v2m) % n, (v2m * v + D * u * u2m) % n
#                 qm = (qm * qkd) % n
#         return u

#     D_abs = abs(D)
#     while jacobi(D, n) != -1:
#         D -= 2 if D > 0 else -2
#         if D_abs + D == 0:
#             D -= 2 if D > 0 else -2
#         D_abs += 2

#     k = n + 1
#     return mod_lucas_seq(n, P, Q, k) == 0


# prime_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

# def baillie_psw(n):
#     if n < 2:
#         return False
#     if n < 4:
#         return True
#     if any(n % p == 0 for p in prime_tuple):
#         return n in prime_tuple
#     if not miller_rabin(n):
#         return False
#     return lucas_probable_prime(n, 3)

# # Example usage:
# n = 103
