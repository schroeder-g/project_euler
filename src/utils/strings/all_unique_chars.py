def all_unique(string):
    h = {}

    for char in string:
        h[char] = h.get(char, 0) + 1

    return max(h.values()) == 1


print(all_unique("abcdefgg"))
