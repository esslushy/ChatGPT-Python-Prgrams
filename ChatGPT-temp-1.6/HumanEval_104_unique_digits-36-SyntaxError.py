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
    Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.

    Args:
    x (List[int]): List of integers.

    Returns:
    List[int]: List of integers with no even digit.
    """

    def has_even_digits(n):
        """
        Returns True if a number contains an even digit, else False.

        Args:
        n (int): The input number.

        Returns:
        bool: True if the number has even digit, else False.
        """
        while n > 0:
            if (n % 10) % 2 == 0:
                return True
            n //= 10
        return False

    # Creating a set of unique digits and returning sorted result
    return sorted(list(set([elem for elem in x if not has_even_digits(elem)]))))

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
