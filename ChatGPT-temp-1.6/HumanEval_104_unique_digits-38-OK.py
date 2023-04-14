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
    def has_even_digit(num: int) -> bool:
        """
        Returns True if num contains at least one even digit, else False.
        """
        while num > 0:
            if (num % 10) % 2 == 0:
                return True
            num //= 10
        return False

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
