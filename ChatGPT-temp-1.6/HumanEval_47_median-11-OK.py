from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    """
    Return the median of the elements in the input list l.

    Args:
    l -- an input list of integers

    Returns:
    The median of the input list l as a float.

    Example:
    median([1,2,3]) -> 2.0
    median([1,2,3,4]) -> 2.5
    median([-10, 4, 6, 1000, 10, 20]) -> 12.0

    """
    sorted_list = sorted(l)  # sort the input list

    n = len(sorted_list)
    if n % 2 == 0:
        # if the number of elements is even, the median is the average of the middle two elements
        return (sorted_list[n//2-1] + sorted_list[n//2])/2
    else:
        # if the number of elements is odd, the median is the middle element
        return sorted_list[n//2]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
