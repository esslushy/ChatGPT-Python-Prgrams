def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """
    # If n is less than 8, it cannot be written as the sum of 4 even numbers
    if n < 8:
        return False
    
    # If n is even, it can be written as the sum of 4 even numbers
    if n % 2 == 0:
        return True
    
    # If n is odd, we can subtract 8 from it and check if the result is even
    return (n - 8) % 2 == 0

def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True

def test_check():
    check(is_equal_to_sum_even)

test_check()
