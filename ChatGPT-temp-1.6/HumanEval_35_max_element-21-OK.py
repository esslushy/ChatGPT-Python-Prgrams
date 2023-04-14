from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    """
    Return maximum element in the list.
    """
    if not l:  # if the list is empty, return None
        return None
    max_num = l[0]  # initialize max_num to first element of the list
    for num in l:
        if num > max_num:  # update max_num if a larger element is found
            max_num = num
    return max_num

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
