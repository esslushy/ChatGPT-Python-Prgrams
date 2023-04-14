from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    """
    Return the maximum element in the list.

    :param l: List of integers.
    :type l: list
    :return: Maximum element in the list.
    :rtype: int
    """
    max_val = float('-inf')
    for i in l:
        if i > max_val:
            max_val = i
    return max_val

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
