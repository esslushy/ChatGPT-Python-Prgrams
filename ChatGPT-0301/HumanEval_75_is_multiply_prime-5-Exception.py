def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """Helper function to check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a: int) -> bool:
    """Function to check if a number is the multiplication of 3 prime numbers"""
    primes = []
    for i in range(2, a):
        if is_prime(i):
            primes.append(i)
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            for k in range(j+1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
    return False

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
