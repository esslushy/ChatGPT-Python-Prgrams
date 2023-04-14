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
    Given a list of positive integers x, return a sorted list of all elements that 
    do not contain any even digit.
    
    Parameters
    ----------
    x : List[int]
        A list of positive integers.

    Returns
    -------
    List[int]
        A sorted list of all elements that does not contain any even digit.

    Examples
    --------
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def has_even_digits(num):
        """
        A helper function that returns True if a given number contains at least
        one even digit.

        Parameters
        ----------
        num : int
            A positive integer.

        Returns
        -------
        bool
            True if a given number contains at least one even digit, else False.
        """

        for digit in str(num):
            if int(digit) % 2 == 0:
                return True
        return False

    return sorted([num for num in x if not has_even_digits(num)])

def check(candidate):
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

def test_check():
    check(unique_digits)

test_check()
