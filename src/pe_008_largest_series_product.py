from math import prod


def get_largest_product_in_series(n, seq):
    m_ = 0
    n = str(n)
    for i in range(len(n)):
        product = prod(([int(s) for s in n[i : seq + i]]))
        if product > m_:
            m_ = product

    print(m_)
