from strings.is_palindrome import is_palindrome


def get_sum_doubly_palindromic_nums():
    return sum(
        [
            num if is_palindrome(str(num)) and is_palindrome(str(bin(num)[2:])) else 0
            for num in range(1, 1000000)
        ]
    )
