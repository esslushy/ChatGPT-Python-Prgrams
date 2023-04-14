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
    Return true if a given number is prime, and false otherwise.
    """
    if n < 2: # Numbers less than 2 are not prime
        return False
    elif n == 2: # 2 is the only even prime number
        return True 
    elif n % 2 == 0: # Other even numbers are not prime
        return False 
    else: # Check if odd number is prime or not
        for i in range(3, int(n**0.5)+1, 2):
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
