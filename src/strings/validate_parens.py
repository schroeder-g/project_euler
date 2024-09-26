def validate_parens(s):
    opening_p = 0
    closing_p = 0
    for char in s:
        prev_open = opening_p
        prev_closing = closing_p
        if ord(char) == 40:
            opening_p += 1
            if prev_closing > prev_open:
                return False
        else:
            closing_p += 1

    return True if opening_p == closing_p else False


print(validate_parens("(())"))
