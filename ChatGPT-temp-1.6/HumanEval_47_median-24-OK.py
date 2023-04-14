from typing import List

def median(l: List[int]) -> float:
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_list = sorted(l)
    length = len(sorted_list)
    middle = length // 2
    if length % 2 == 0:
        # If the length of the list is even, average the two middle elements
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2
    else:
        # If the length of the list is odd, return the middle element
        return sorted_list[middle]

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
