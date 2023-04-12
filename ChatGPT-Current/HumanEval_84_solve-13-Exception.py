def solve(N: int) -> str:
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
    >>> solve(1000)
    '1'
    >>> solve(150)
    '110'
    >>> solve(147)
    '1100'
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    binary_sum = 0
    while N > 0:
        binary_sum += N % 2
        N //= 2
    return bin(binary_sum)[2:]

def check(candidate):
    assert candidate(1000) == '1'
    assert candidate(150) == '110'
    assert candidate(147) == '1100'
    assert candidate(333) == '1001'
    assert candidate(963) == '10010'

def test_check():
    check(solve)

test_check()
