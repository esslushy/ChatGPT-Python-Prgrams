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
    Returns the largest index of an element which is not greater than or equal
    to the element immediately preceding it. If no such element exists then
    return -1.

    The given array will not contain duplicate values.

    Args:
        arr: A list of integers

    Returns:
        The largest index of an element which is not greater than or equal to the
        element immediately preceding it. If no such element exists then return -1.
    """
    if len(arr) < 2:
        # Not enough elements to make a comparison, so return -1
        return -1

    last = arr[0]
    res = -1

    for i in range(1, len(arr)):
        if arr[i] >= last:
            # Element at index i is greater than or equal to element at index i-1
            last = arr[i]
        else:
            # Element at index i is smaller than element at index i-1
            res = i - 1

    return res

def check(candidate):
    assert candidate([1, 2, 4, 3, 5]) == 3
    assert candidate([1, 2, 4, 5]) == -1
    assert candidate([1, 4, 2, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate([4, 8, 5, 7, 3]) == 4
    assert candidate([]) == -1

def test_check():
    check(can_arrange)

test_check()
