def gen_distinct_consecutive_products(range_a, range_b):
    seq = [a**b for a in range(2, range_a) for b in range(2, range_b)]

    return len(set(seq))
