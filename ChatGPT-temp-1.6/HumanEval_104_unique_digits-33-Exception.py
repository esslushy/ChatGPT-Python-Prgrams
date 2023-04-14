from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    """Helper function that returns True if n contains an even digit."""
    for digit in str(n):
        if int(digit) % 2 == 0:
            return True
    return False

def unique_digits(x: List[int]) -> List[int]:
    """Returns a sorted list of all elements in x that haven't any even digit."""
    result = []
    for num in x:
        if not has_even_digit(num):
            result.append(num)
    return sorted(result)

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
