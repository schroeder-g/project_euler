def find_longest_consecutive_subsequence(arr):
    len_ = len(arr)

    if len_ == 0 or len_ == 1:
        return len_

    ans, current_seq = 1, 1

    # create sorted list of non-repeating values
    s = sorted(list(set(arr)))

    for i in range(len(s) - 1):
        if s[i + 1] == s[i] + 1:
            current_seq += 1
        else:
            current_seq = 1
        if current_seq > ans:
            ans = current_seq

    return ans


test = [-1, 2, 1, 0, 1, 2, 3]
print(
    "the longest consecutive subsequence is", find_longest_consecutive_subsequence(test)
)
