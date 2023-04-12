def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """Returns True if the given number is the multiplication of 3 prime numbers, False otherwise."""
    if a < 2:
        return False
    primes = []
    i = 2
    while len(primes) < 3 and i * i <= a:
        if a % i == 0:
            primes.append(i)
            a //= i
        else:
            i += 1
    if a > 1:
        primes.append(a)
    return len(primes) == 3

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
