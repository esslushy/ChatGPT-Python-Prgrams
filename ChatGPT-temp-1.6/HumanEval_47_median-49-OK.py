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
    """
    sorted_l = sorted(l)
    length = len(sorted_l)
    
    # If the list has an odd number of elements, return the middle one.
    if length % 2 == 1:
        return sorted_l[length//2]
    
    # If the list has an even number of elements, return the average of the two middle ones.
    else:
        left_middle = sorted_l[length//2 - 1]
        right_middle = sorted_l[length//2]
        return (left_middle + right_middle) / 2

def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7

def test_check():
    check(median)

test_check()
