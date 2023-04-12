def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """
    Returns True if the given number is the multiplication of 3 prime numbers, False otherwise.
    """
    # Check if the number is less than 2, which is not a prime number
    if a < 2:
        return False
    
    # Check if the number is 2 or 3, which are prime numbers
    if a == 2 or a == 3:
        return True
    
    # Check if the number is divisible by 2 or 3, which are not prime numbers
    if a % 2 == 0 or a % 3 == 0:
        return False
    
    # Check if the number is the multiplication of 3 prime numbers
    i = 5
    while i * i <= a:
        if a % i == 0 or a % (i + 2) == 0:
            return False
        i += 6
    return True

def check(candidate):
    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(105) == True
    assert candidate(126) == False
    assert candidate(729) == False
    assert candidate(891) == False
    assert candidate(1001) == True

def test_check():
    check(is_multiply_prime)

test_check()
