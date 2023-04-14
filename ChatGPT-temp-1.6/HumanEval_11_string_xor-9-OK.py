def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """
    Inputs are two strings a and b consisting only of 1s and 0s.
    Performs binary XOR on these inputs and returns result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Padding with leading zeroes to ensure both strings are of equal length
    a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))
    result = ''
    
    # Performing binary XOR
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
