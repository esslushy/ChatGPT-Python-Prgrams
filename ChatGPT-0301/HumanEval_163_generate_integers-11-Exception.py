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
    result = []
    for num in range(a, b+1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                result.append(int(digit))
    return sorted(list(set(result)))

def check(candidate):
    assert candidate(2, 10) == [2, 4, 6, 8]
    assert candidate(10, 2) == [2, 4, 6, 8]
    assert candidate(132, 2) == [2, 4, 6, 8]
    assert candidate(17, 89) == []

def test_check():
    check(generate_integers)

test_check()
