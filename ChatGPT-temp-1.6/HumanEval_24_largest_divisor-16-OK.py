def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    """
    For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Examples:
    largest_divisor(15) -> 5
    largest_divisor(12) -> 6
    
    Args:
    n (int): a positive integer
    
    Returns:
    int: the largest number that divides n evenly, smaller than n
    """
    # We start looking from n-1 down to 1 (exclusive)
    for i in range(n - 1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i
    # If we reach the end of the loop without finding a divisor, return None or raise an error
    return None

def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
