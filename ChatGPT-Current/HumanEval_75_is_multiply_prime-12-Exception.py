def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """
    """Returns True if the given number is the multiplication of 3 prime numbers and False otherwise."""
    
    # Check if the number is less than 2 or greater than 97
    if a < 2 or a > 97:
        return False
    
    # Check if the number is divisible by 2, 3, or 5
    if a % 2 == 0 or a % 3 == 0 or a % 5 == 0:
        # If it is, check if it's equal to the product of 2, 3, and another prime number
        for i in range(7, a):
            if a % i == 0 and is_prime(i) and is_prime(a // i):
                return True
        return False
    
    # If the number is not divisible by 2, 3, or 5, check if it's equal to the product of 3 prime numbers
    primes = []
    i = 2
    while len(primes) < 3 and i <= a:
        if is_prime(i) and a % i == 0:
            primes.append(i)
            a //= i
        else:
            i += 1
    return len(primes) == 3 and is_prime(a) and a not in primes


def is_prime(n: int) -> bool:
    """Returns True if the given number is prime and False otherwise."""
    
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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
