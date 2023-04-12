from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    # Swap a and b if a is greater than b
    if a > b:
        a, b = b, a

    # Create an empty list to store even digits
    even_digits = []

    # Loop through each number between a and b
    for num in range(a, b+1):
        # Convert the number to a string to access each digit
        num_str = str(num)
        # Loop through each digit in the number
        for digit in num_str:
            # Check if the digit is even and not already in the list
            if int(digit) % 2 == 0 and int(digit) not in even_digits:
                even_digits.append(int(digit))

    # Sort the list in ascending order
    even_digits.sort()

    return even_digits

def check(candidate):
    assert candidate(2, 10) == [2, 4, 6, 8]
    assert candidate(10, 2) == [2, 4, 6, 8]
    assert candidate(132, 2) == [2, 4, 6, 8]
    assert candidate(17, 89) == []

def test_check():
    check(generate_integers)

test_check()
