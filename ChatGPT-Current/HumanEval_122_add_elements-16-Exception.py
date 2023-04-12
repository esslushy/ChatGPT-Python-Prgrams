from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(x for x in arr[:k] if x >= 10 and x <= 99)

def check(candidate):
    assert candidate([1, -2, -3, 41, 57, 76, 87, 88, 99], 3) == -4
    assert candidate([111, 121, 3, 4000, 5, 6], 2) == 0
    assert candidate([11, 21, 3, 90, 5, 6, 7, 8, 9], 4) == 125
    assert candidate([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24
    assert candidate([1], 1) == 1

def test_check():
    check(add_elements)

test_check()
