import numpy as np


# NOTE: Doesn't work as advertised
def multiply_series(series):
    powers = [np.array(s) for s in series]
    current_counts = np.ones(len(powers[0]))
    current_powers = powers[0]

    # For each element in the first series, multiply it with each element in others
    for p in powers[1:]:
        powers_to_add = []
        for el in p:
            power_mult = []
            for curr_pow, curr_count in list(zip(current_powers, current_counts)):
                el_to_add = [curr_pow + el] * int(curr_count)
                # Append each multiplied power element * count times
                power_mult.extend(el_to_add)

            powers_to_add.extend(power_mult)
        current_powers, current_counts = np.unique(powers_to_add, return_counts=True)
    return list(zip(current_powers, current_counts))


def series_multiplication(powers):
    powers = [np.array(p) for p in powers]
    current_counts = np.ones(len(powers[0]))
    current_powers = powers[0]

    for p in powers[1:]:
        """
        multiply each element from the first series with each element in the other series
        """
        powers_to_add = []
        for e in p:
            power_mult = list(current_powers + e)
            for cp, cc in list(zip(current_powers, current_counts)):
                elements_to_add = [cp + e] * int(cc)
                # append each multiplied cp element cc times
                power_mult.extend(elements_to_add)
            powers_to_add.extend(power_mult)
        current_powers, current_counts = np.unique(powers_to_add, return_counts=True)
    return list(zip(current_powers, current_counts))
