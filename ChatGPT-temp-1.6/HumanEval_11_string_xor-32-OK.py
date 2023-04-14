def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """
    Performs a binary XOR operation on two binary strings a and b.
    
    Parameters:
    a (str): A binary string containing only 0s and 1s.
    b (str): A binary string containing only 0s and 1s.
    
    Returns:
    str: A binary string obtained after XOR operation between the inputs.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('1010', '0111')
    '1101'
    """
    result = ''
    for i in range(len(a)):
        # XOR of two bits can be performed by using the bitwise XOR operator ^.
        result += str(int(a[i]) ^ int(b[i]))
    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
