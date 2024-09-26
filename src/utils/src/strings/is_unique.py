def all_unique_characters(s):
    h = {}
    for char in s:
        if char in h:
            return False
        else:
            h[char] = 1
    return True
