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
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 8:
        return False
    for i in range(2, n-2, 2):
        for j in range(i, n-i-2, 2):
            for k in range(j, n-i-j-2, 2):
                if i+j+k+(n-i-j-k) == n:
                    return True
    return False

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
