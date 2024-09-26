def removeAdjacent(s):
    noidenticals = ""
    if len(list(s)) > 0:
        noidenticals = list(s)[0]
        for i, char in enumerate(s):
            if char != list(s)[i - 1] and i != 0:
                noidenticals += char
    return str(noidenticals)


print(removeAdjacent("aaaabbaaaa"))
