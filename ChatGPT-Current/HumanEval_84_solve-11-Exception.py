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
    # convert N to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # sum the digits in binary
    binary_sum = sum(int(digit) for digit in binary)
    
    # convert the binary sum back to binary and return as a string
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
