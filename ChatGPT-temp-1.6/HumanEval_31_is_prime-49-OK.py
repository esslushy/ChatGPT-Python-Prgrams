def is_prime(n: int) -> bool:
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    """
    Return True if n is a prime number, False otherwise.
    A number is considered prime if it has exactly two divisors, 1 and itself.
    """
    # Check if the number is less than 2
    if n < 2:
        return False
    
    # Check for divisors from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def check(candidate):
    assert candidate(6) == False
    assert candidate(101) == True
    assert candidate(11) == True
    assert candidate(13441) == True
    assert candidate(61) == True
    assert candidate(4) == False
    assert candidate(1) == False
    assert candidate(5) == True
    assert candidate(11) == True
    assert candidate(17) == True
    assert candidate(85) == False
    assert candidate(77) == False
    assert candidate(255379) == False

def test_check():
    check(is_prime)

test_check()
