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
    # traverse the array from right to left to find the largest index i where arr[i-1] > arr[i]
    n = len(arr)
    i = n - 1
    while i > 0 and arr[i-1] <= arr[i]:
        i -= 1

    # if no such i exists, return -1
    if i == 0:
        return -1

    # traverse the array from right to left to find the largest index j where arr[i-1] > arr[j]
    j = i - 1
    while j+1 < n and arr[j+1] < arr[i-1]:
        j += 1

    # swap arr[i-1] with arr[j]
    arr[i-1], arr[j] = arr[j], arr[i-1]

    # reverse the elements from i to n-1 in the array
    arr[i:] = reversed(arr[i:])

    # return the value of i-1
    return i-1

def check(candidate):
    assert candidate([1, 2, 4, 3, 5]) == 3
    assert candidate([1, 2, 4, 5]) == -1
    assert candidate([1, 4, 2, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate([4, 8, 5, 7, 3]) == 4
    assert candidate([]) == -1

def test_check():
    check(can_arrange)

test_check()
