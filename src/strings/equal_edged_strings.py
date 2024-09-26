# For each string in an array, return true if the first and last letter of the string
# are identical the following index.


def equal_edged_strings(words):
    return [
        words[i][0] == words[i + 1][0] and words[i][-1] == words[i + 1][-1]
        for i in range(len(words) - 1)
    ]


test = ["abcd", "ad", "aaa", "aba"]

print(equal_edged_strings(test))
