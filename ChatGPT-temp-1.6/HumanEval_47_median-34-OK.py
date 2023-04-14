from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    Return the median value of the given list of integers.

    Args:
    - l (List[int]): a list of integers

    Returns:
    - float: the median value of the given list of integers
    """

    # sort the list in non-decreasing order
    sorted_l = sorted(l)

    # find the middle index of the list
    n = len(l)
    mid_idx = n // 2

    # if the length of the list is odd
    if n % 2 != 0:
        # return the middle element of the sorted list
        return sorted_l[mid_idx]
    # if the length of the list is even
    else:
        # calculate the average of the two middle elements of the sorted list
        return (sorted_l[mid_idx-1] + sorted_l[mid_idx]) / 2

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
