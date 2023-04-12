def is_simple_power(x: int, n: int) -> bool:
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    >>> is_simple_power(1, 4)
    True
    >>> is_simple_power(2, 2)
    True
    >>> is_simple_power(8, 2)
    True
    >>> is_simple_power(3, 2)
    False
    >>> is_simple_power(3, 1)
    False
    >>> is_simple_power(5, 3)
    False
    """
    """
    Returns true if a number x is a simple power of n and false in other cases.
    x is a simple power of n if n**int=x
    """
    if x == 1:
        return True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            p = i
            e = 0
            while x % p == 0:
                x //= p
                e += 1
            if x == 1 and e % n == 0:
                return True
            break
    else:
        if x > 1 and x == n:
            return True
    return False

def check(candidate):
    assert candidate(16, 2) == True
    assert candidate(143214, 16) == False
    assert candidate(4, 2) == True
    assert candidate(9, 3) == True
    assert candidate(16, 4) == True
    assert candidate(24, 2) == False
    assert candidate(128, 4) == False
    assert candidate(12, 6) == False
    assert candidate(1, 1) == True
    assert candidate(1, 12) == True

def test_check():
    check(is_simple_power)

test_check()
