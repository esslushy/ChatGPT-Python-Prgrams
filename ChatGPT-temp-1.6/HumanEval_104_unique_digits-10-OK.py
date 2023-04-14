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
    """
    Given a list of positive integers x, return a sorted list of all elements
    that don't contain an even digit.
    """
    result = []
    for number in x:
        digits = set(str(number))
        has_even_digit = any(int(digit) % 2 == 0 for digit in digits)
        if not has_even_digit:
            result.append(number)
    return sorted(result)

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
