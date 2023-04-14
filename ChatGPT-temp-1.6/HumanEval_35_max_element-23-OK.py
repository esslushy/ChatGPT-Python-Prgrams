from typing import List

def max_element(l: List[int]) -> int:
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Initialize max_element to the first element in the list
    max_element = l[0]
    
    # Compare each subsequent element with the current max_element
    # and update max_element if a larger element is found
    for num in l[1:]:
        if num > max_element:
            max_element = num
    
    return max_element

def check(candidate):
    assert candidate([1, 2, 3]) == 3
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124

def test_check():
    check(max_element)

test_check()
