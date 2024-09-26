# An algorithm to find all occurrences of a given pattern in a text.

q = 101  # A nice prime
d = 256  # number of characters in ASCII


def rabin_karp(pat, txt, q):
    ans = []
    n, m = len(txt), len(pat)
    h = 1  # initialize our hashing variable
    p, t = 0, 0  # initialize hashes for pattern and text window

    # determine hash value
    for _ in range(m - 1):
        h = (d * h) % q

    # hash the pattern as well as the first text window
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # iterate through all windows in text looking for a match
    for i in range(n - m + 1):
        if p == t:  # in the case that they do match:
            for j in range(m):  # iterate through each character in pattern and
                if pat[j] != txt[i + j]:  # text window, comparing them.
                    break
                else:
                    j += 1
            if (
                j == m
            ):  # reaching end of window, there were no deviations between pattern and substring.
                ans.append(str(i))
        # at the end of each iteration, must rehash for the next text window.
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if t < 0:
                t = t + q

    return ans


pattern = "ll"
text = "hello"

print(rabin_karp(pattern, text, q))
