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
    l (List[int]): List of integers to calculate median of.

    Returns:
    float: Median of the given list of integers.

    Examples:
    >>> median([3, 1, 2, 4, 5])
    3.0
    >>> median([-10, 4, 6, 1000, 10, 20])
    7.0
    """

    n = len(l)
    s = sorted(l)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2.0
    else:
        return s[mid]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
