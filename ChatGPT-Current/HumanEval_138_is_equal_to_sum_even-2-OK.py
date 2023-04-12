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
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    """
    if n % 2 != 0 or n < 8:
        # If n is odd or less than 8, it cannot be written as the sum of 4 positive even numbers
        return False
    
    # Check all possible combinations of 4 positive even numbers that add up to n
    for i in range(2, n//2 + 1, 2):
        for j in range(2, n//2 + 1, 2):
            for k in range(2, n//2 + 1, 2):
                for l in range(2, n//2 + 1, 2):
                    if i + j + k + l == n:
                        return True
    
    # If no combination of 4 positive even numbers adds up to n, return False
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
