MAX_CHARS = 256


def csIsomorphicStrings(string1, string2):
    """
    2) For every character in str1 and str2:
         a) If this character is seen first time in str1,
            then current of str2 must have not appeared before.
            (i) If current character of str2 is seen, return false.
              Mark current character of str2 as visited.
            (ii) Store mapping of current characters.
        b) Else check if previous occurrence of str1[i]
             is mapped to previous character
    """
    m = len(string1)
    n = len(string2)
    # Length of both strings must be same for one to one correspondence
    if m != n:
        return False

    # To mark visited characters in str2
    marked = [False] * MAX_CHARS

    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS

    # Process all characters one by one
    for i in range(n):

        # if current character of str1 is seen first
        # time in it.
        if map[ord(string1[i])] == -1:

            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(string2[i])]:
                return False

            # Mark current character of str2 as visited
            marked[ord(string2[i])] = True

            # Store mapping of current characters
            map[ord(string1[i])] = string2[i]

        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(string1[i])] != string2[i]:
            return False

    return True
