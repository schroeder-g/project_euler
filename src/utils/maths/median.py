def median(sequence):
    quotient, remainder = divmod(len(sequence), 2)
    if remainder:
        return sorted(sequence)[quotient]
    return sum(sorted(sequence)[quotient - 1 : quotient + 1]) / 2.0


if __name__ == "__main__":
    nums = [
        int(n.strip())
        for n in input("Enter a comma delimited list of numbers: ").split(",")
    ]
    print(f"the median is: {median(nums)}")
