def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    """For a given number n, find the largest number that divides n evenly, smaller than n
    
    Args:
    n (int): A positive integer
    
    Returns:
    int: The largest divisor of n
    
    Examples:
    >>> largest_divisor(15)
    5
    """
    divisor = n-1
    
    while divisor > 1:
        if n % divisor == 0:
            return divisor
        else:
            divisor -= 1
    
    return -1 # If no divisor is found

def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
