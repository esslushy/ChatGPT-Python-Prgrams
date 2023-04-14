from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:
        # if the list is empty, return None
        return None
    max_value = l[0] # initialize max_value to the first element
    for x in l:
        # for each element in the list, check if it is greater than the current max_value
        if x > max_value:
            max_value = x # update max_value if the element is greater
    return max_value

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
