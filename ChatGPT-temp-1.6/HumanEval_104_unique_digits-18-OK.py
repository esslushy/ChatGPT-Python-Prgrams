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
    unique_nums = []
    for num in x:
        # convert integer to string for easy manipulation of digits
        num_str = str(num)
        # check if any digit is even
        if all(int(digit) % 2 != 0 for digit in num_str):
            unique_nums.append(num)
    
    return sorted(unique_nums)

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
