def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n-1, 0, -1):  # start from n-1 and go backwards
        if n % i == 0:  # if i divides n evenly
            return i   # return i as the largest divisor
    return 1   # if no divisor is found, return 1 as the default

def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
