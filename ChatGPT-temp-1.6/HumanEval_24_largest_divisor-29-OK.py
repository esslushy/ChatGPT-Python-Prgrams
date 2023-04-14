def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    """
    Given an integer n, this function finds the largest integer that can divide n 
    evenly, where this integer should be smaller than n.
    """
    for i in range(n-1, 0, -1):   # iterating backwards from n-1 to 1
        if n % i == 0:    # checking if i divides n evenly 
            return i
    return None  # when no divisor is found, None is returned.

def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
