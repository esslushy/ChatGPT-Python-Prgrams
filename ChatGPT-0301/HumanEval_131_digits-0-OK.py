def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """
    product = 1
    has_odd_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
            has_odd_digit = True
        n //= 10
    if has_odd_digit:
        return product
    else:
        return 0

def check(candidate):
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) == 1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625
    assert candidate(2468) == 0

def test_check():
    check(digits)

test_check()
