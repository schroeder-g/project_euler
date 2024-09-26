def is_integral(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
