def score_word(name):
    return sum([ord(char) - 64 for char in name])
