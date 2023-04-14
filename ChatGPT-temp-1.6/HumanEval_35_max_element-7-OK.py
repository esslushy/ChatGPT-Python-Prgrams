from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # check that list is not empty
    if not l:
        raise ValueError("list is empty")
    
    # initialize max_element to the first element of the list
    max_element = l[0]
    
    # iterate over the rest of the list
    for element in l[1:]:
        # if we find a new maximum element, update the max_element variable
        if element > max_element:
            max_element = element
    
    # return the maximum element
    return max_element

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
