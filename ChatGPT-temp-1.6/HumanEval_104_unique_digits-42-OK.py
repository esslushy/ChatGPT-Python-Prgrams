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
    that hasn't any even digit.

    Parameters:
    x (List[int]): List of positive integers

    Returns:
    List[int]: List of sorted integers containing no even digits

    Example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # List to hold the filtered integers with odd digits
    odd_digit_ints = []
    
    for integer in x:
        str_int = str(integer)
        has_even_digit = False
        for char in str_int:
            if int(char) % 2 == 0:
                has_even_digit = True
                break
        
        # Add to the list only if the integer has no even digit
        if not has_even_digit:
            odd_digit_ints.append(integer)
    
    # Return the sorted list of integers with no even digit
    return sorted(odd_digit_ints)

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
