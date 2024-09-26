def checkBlanagrams(word1, word2):
    sorted_1 = sorted(word1)
    sorted_2 = sorted(word2)

    num_different = 0

    if sorted_1 == sorted_2:
        return False

    for i in range(len(word1)):

        if sorted_1[i] != sorted_2[i]:
            num_different += 1
        if num_different == 2:
            return False
        else:
            return True
