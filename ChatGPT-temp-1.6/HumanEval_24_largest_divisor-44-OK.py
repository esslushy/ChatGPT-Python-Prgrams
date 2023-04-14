def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    largest_div = n - 1  # initialize the largest divisor as n - 1
    while largest_div > 0:  # keep looping until we find the largest divisor
        if n % largest_div == 0:  # check if the current largest divisor evenly divides n
            return largest_div
        largest_div -= 1  # if not, decrement the largest divisor and try again
    return largest_div  # if we've looped through all possible divisors and still haven't found a match, return the largest divisor (which will be 1)

def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

def test_check():
    check(largest_divisor)

test_check()
