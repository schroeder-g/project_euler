def csWordPattern(pattern, a):
    sliced_words = a.split()
    pattern_list = list(pattern)

    if len(pattern) != len(sliced_words):
        return False
    elif len(pattern) == 0:
        return True

    w2p = {}
    p2w = {}

    for i in range(0, len(sliced_words)):
        w = sliced_words[i]
        p = pattern_list[i]
        if w in w2p and p in p2w:
            if w2p[w] != p or p2w[p] != w:
                return False
        elif w in w2p or p in p2w:
            return False
        else:
            p2w[p] = w
            w2p[w] = p

    return True


pattern = "abcda"
string = "rock on big daddy rock"
print(csWordPattern(pattern, string))
