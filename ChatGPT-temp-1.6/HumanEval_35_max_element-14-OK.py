from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Handle empty list case
    if len(l) == 0:
        raise ValueError("Cannot find max of empty list")

    max_num = l[0] # Set the maximum to be the first element in the list
    for num in l:
        if num > max_num:
            max_num = num # Update the maximum if we find a larger element
    return max_num

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
