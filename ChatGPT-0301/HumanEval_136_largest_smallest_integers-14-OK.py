from typing import List, Tuple, Optional

def largest_smallest_integers(lst: List[int]) -> Tuple[Optional[int], Optional[int]]:
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    >>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
    (None, 1)
    >>> largest_smallest_integers([])
    (None, None)
    >>> largest_smallest_integers([0])
    (None, None)
    """
    pos_ints = [i for i in lst if i > 0]
    neg_ints = [i for i in lst if i < 0]
    if not pos_ints:
        smallest_pos = None
    else:
        smallest_pos = min(pos_ints)
    if not neg_ints:
        largest_neg = None
    else:
        largest_neg = max(neg_ints)
    return (largest_neg, smallest_pos)

def check(candidate):
    assert candidate([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert candidate([2, 4, 1, 3, 5, 7, 0]) == (None, 1)
    assert candidate([1, 3, 2, 4, 5, 6, -2]) == (-2, 1)
    assert candidate([4, 5, 3, 6, 2, 7, -7]) == (-7, 2)
    assert candidate([7, 3, 8, 4, 9, 2, 5, -9]) == (-9, 2)
    assert candidate([]) == (None, None)
    assert candidate([0]) == (None, None)
    assert candidate([-1, -3, -5, -6]) == (-1, None)
    assert candidate([-1, -3, -5, -6, 0]) == (-1, None)
    assert candidate([-6, -4, -4, -3, 1]) == (-3, 1)
    assert candidate([-6, -4, -4, -3, -100, 1]) == (-3, 1)

def test_check():
    check(largest_smallest_integers)

test_check()
