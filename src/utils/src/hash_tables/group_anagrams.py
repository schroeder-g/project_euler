def csGroupAnagrams(strs):
    result = {}
    for i in strs:
        x = "".join(sorted(i))
        if x in result:
            result[x].append(i)
        else:
            result[x] = [i]
    return list(result.values())


words = ["apt", "pat", "ear", "tap", "are", "arm"]
print(csGroupAnagrams(words))
