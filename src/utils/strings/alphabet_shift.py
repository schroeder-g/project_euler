def alphabeticShift(inputString):
    new_string = ""
    for char in inputString:
        print(ord(char))
        if 97 <= ord(char) < 122:
            new_string += chr(ord(char) + 1)
        elif ord(char) == 122:
            new_string += "a"
    return new_string


inputt = "abcdefg"
print(alphabeticShift(inputt))
