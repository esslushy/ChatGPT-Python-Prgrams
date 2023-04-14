from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        raise ValueError("Cannot find maximum element in empty list.")
    max_so_far = l[0]
    for num in l:
        if num > max_so_far:
            max_so_far = num
    return max_so_far

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
