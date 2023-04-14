from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """Return median of elements in the list l."""
    sorted_list = sorted(l)  # sort the input list in ascending order
    n = len(sorted_list)
    mid = n // 2  # calculate the middle index

    if n % 2 == 0:  # even-length list, median is average of middle two elements
        return (sorted_list[mid-1] + sorted_list[mid]) / 2.0
    else:  # odd-length list, median is middle element
        return sorted_list[mid]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
