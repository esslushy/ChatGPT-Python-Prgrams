from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l_sorted = sorted(l)
    n = len(l_sorted)
    if n % 2 == 0:
        # if the list has an even number of elements,
        # we return the average of the middle two
        # (Note: we subtract 1 from n because lists are zero-indexed)
        return (l_sorted[(n // 2) - 1] + l_sorted[n // 2]) / 2.0
    else:
        # if the list has an odd number of elements, we return the middle one
        return l_sorted[n // 2]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
