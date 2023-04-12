def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 1:
        return 2
    else:
        count += 2 * (9 * 10 ** (n - 2))
        count += starts_one_ends(n - 1)
    return count

def check(candidate):
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

def test_check():
    check(starts_one_ends)

test_check()
