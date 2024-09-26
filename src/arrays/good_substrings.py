def almost_ordered_list(sequence):
    num_out_of_order = 0
    for index, num in enumerate(sequence):
        if index != 0 and num <= sequence[index - 1]:
            num_out_of_order += 1
    if num_out_of_order > 1:
        return False
    else:
        return True


increasing_seq = [1, 2, 1, 2]
print(almost_ordered_list(increasing_seq), "\n")
