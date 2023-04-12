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
    # Check if the number is less than 2
    if a < 2:
        return False
    
    # Check if the number is equal to 2, 3, or 5
    if a in [2, 3, 5]:
        return True
    
    # Check if the number is divisible by 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        return False
    
    # Check if the number is the multiplication of 3 prime numbers
    count = 0
    for i in range(2, int(a/2)+1):
        if a % i == 0:
            count += 1
            if count > 2:
                return False
            if is_prime(i) and is_prime(int(a/i)):
                return True
    return False

def is_prime(n: int) -> bool:
    """
    Returns True if the given number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
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
