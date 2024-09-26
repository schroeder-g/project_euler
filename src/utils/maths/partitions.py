from itertools import permutations


def partitions(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        left = k + 1
        while x <= y:
            a[k] = x
            a[left] = y
            yield a[: k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[: k + 1]


def simple_partitions(n, vals):
    yield n,
    for i in vals:
        if i < n:
            for p in simple_partitions(n - i, vals):
                yield [i] + list(p)


def get_k_integer_partitions(n, k, max_value=None):
    if max_value is None:
        max_value = n
    if k == 1:
        if 1 <= n <= max_value:
            yield [n]
        return
    for i in range(min(max_value, n - k + 1), 0, -1):
        for tail in get_k_integer_partitions(n - i, k - 1, i):
            yield [i] + tail


def get_integer_partition_permutations(n, k, max_value=None):
    all_permutations = set()

    partitions = list(get_k_integer_partitions(n, k))

    for partition in partitions:
        # Generate all permutations of the current partition
        perms = set(permutations(partition))
        # Add the unique permutations to the overall set
        all_permutations.update(perms)

    # Convert the set to a list and sort it for readability
    all_permutations = sorted(all_permutations)

    return all_permutations
