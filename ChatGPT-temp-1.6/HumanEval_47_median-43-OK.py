from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    Return median of elements in the list l.

    Args:
        l: a list of integers

    Returns:
        the median value of the list l (a float)

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    n = len(l)
    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle one.
        return sorted(l)[n // 2]
    else:
        # If the list has an even number of elements, return the average of the two middle ones.
        return sum(sorted(l)[n // 2 - 1: n // 2 + 1]) / 2

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
