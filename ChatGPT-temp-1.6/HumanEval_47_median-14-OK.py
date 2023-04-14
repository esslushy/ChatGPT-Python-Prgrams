from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """Return median of elements in the list l.
    """
    # first, sort the list
    sorted_l = sorted(l)

    # check if the list has an even or odd number of elements
    n = len(sorted_l)
    if n % 2 == 0:
        # if the length is even, take the average of the two middle elements
        return (sorted_l[n // 2 - 1] + sorted_l[n // 2]) / 2
    else:
        # if the length is odd, return the middle element
        return sorted_l[n // 2]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
