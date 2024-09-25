def smallest_multiple_of_sub_20():
    base = 2520
    is_smallest_multiple = False
    while not is_smallest_multiple:
        # TODO: Don't hardcode these vals
        largest_divisors = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
        for i, div in enumerate(largest_divisors):
            if not is_evenly_divisible(base, div):
                base += 2520
                break

            print(f"{base} % {div} = {base % div}")
            if i == len(largest_divisors) - 1:
                is_smallest_multiple = True

        if not is_smallest_multiple:
            continue

        print(
            f"{base} is evenly divisible by all numbers in the range 1 -> 21:\n"
        )
        for i, div in enumerate(largest_divisors):
            print(f"{base} % {div} = {base % div}")
        is_smallest_multiple = True

        break


def is_evenly_divisible(n, div):
    return n % div == 0
