def clean_non_ascii(text):
    return text.encode("ascii", "ignore").decode("ascii")
