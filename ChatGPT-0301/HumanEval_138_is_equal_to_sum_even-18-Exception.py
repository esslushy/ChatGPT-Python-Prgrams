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
    if n % 2 != 0:
        return False
    for i in range(1, n//2+1):
        for j in range(i, n//2+1):
            for k in range(j, n//2+1):
                if i + j + k == n and (i % 2 == 0) and (j % 2 == 0) and (k % 2 == 0):
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
