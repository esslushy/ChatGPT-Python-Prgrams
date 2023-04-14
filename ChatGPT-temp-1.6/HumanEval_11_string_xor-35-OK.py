def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """
    Inputs: 
    a: A binary string of 1s and 0s
    b: A binary string of 1s and 0s
    Returns:
    A binary string that is the result of performing XOR operation on 'a' and 'b'.
    
    Examples:
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('10101', '11111')
    '01010'
    >>> string_xor('00000', '10101')
    '10101'
    """
    
    if len(a) != len(b):
        raise ValueError("Strings should have the same length")
    
    res = ''
    
    for i in range(len(a)):
        if a[i] == b[i]:
            res += '0'
        else:
            res += '1'
    
    return res

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
