def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """Returns true if the given number is the multiplication of 3 prime numbers and false otherwise."""
    if a < 2:
        return False
    primes = []
    for num in range(2, a+1):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
    return count == 3

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
