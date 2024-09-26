def first_unique_char(string):
    # Your code here
    counts = {}
    # loop through our string to populate dictionary
    # with the counts of each character
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    print(counts)
    # loop over the string again
    # for each char, check how many times it occurs
    # return the index of the first char that occurs once
    for index, char in enumerate(string):
        if counts[char] == 1:
            return index
    # otherwise, no char in the string occurred exactly once
    return -1


string = "Lorem Ipsum"
first_unique_char(string)
