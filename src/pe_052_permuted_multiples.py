def find_permuted_multiples():
    all_ = {}
    RANGE_START = 125874
    # RANGE_START = 125874
    RANGE_END = 166666666
    # RANGE_END = 125877

    for n in range(RANGE_START, RANGE_END):
        st = sorted(str(n))
        perms = set({n})
        for i, m in enumerate(range(2, 7)):
            product = m * n

            if sorted(str(product)) != st:
                break
            else:
                if i > 1:
                    print(i, n, product, perms)
                perms.add(product)

        if len(perms) == 6:
            all_[n] = perms

    print(sorted(all_.items(), key=lambda i: i[0]))


find_permuted_multiples()
