def is_sequence(numbers: [int | float], frequency):
    """
    Check if the list of numbers follows the sequence defined by the frequency generator.

    Parameters:
    - numbers (list of numbers): The sequence to check.
    - frequency (iterable): A generator or iterable that produces the expected sequence.

    Returns:
    - bool: True if numbers match the frequency sequence, False otherwise.
    """
    gen = iter(frequency)  # Ensure frequency is an iterator
    for num in numbers:
        try:
            expected = next(gen)
        except StopIteration:
            # The frequency sequence ended before the numbers list
            return False
        if num != expected:
            return False
    return True


def arithmetic_sequence(start, step):
    """
    Generator for an arithmetic sequence.

    Parameters:
    - start (int): The starting number of the sequence.
    - step (int): The difference between consecutive numbers.

    Yields:
    - int: Next number in the arithmetic sequence.
    """
    current = start
    while True:
        yield current
        current += step
