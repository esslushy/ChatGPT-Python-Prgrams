from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """
    """
    Returns the largest index of an element which is not greater than or equal to
    the element immediately preceding it in the given list. If no such element exists,
    returns -1.
    
    Args:
        arr: A list of integers with no duplicate values
        
    Returns:
        The largest index i where arr[i] is not greater than arr[i-1], or -1 if no such index exists
    
    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """
    n = len(arr)
    if n == 1:      # Only one element in the list
        return -1
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i-1
    return -1

def check(candidate):
    assert candidate([1, 2, 4, 3, 5]) == 3
    assert candidate([1, 2, 4, 5]) == -1
    assert candidate([1, 4, 2, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate([4, 8, 5, 7, 3]) == 4
    assert candidate([]) == -1

def test_check():
    check(can_arrange)

test_check()
