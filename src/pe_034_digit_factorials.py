from math import factorial


def get_digit_factorial():
    return (
        sum(
            [
                sum([factorial(int(i)) for i in str(num)])
                for num in range(5000000)
                if sum([factorial(int(i)) for i in str(num)]) == num
            ]
        )
        - 3
    )
