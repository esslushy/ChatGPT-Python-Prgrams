def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert both strings to integers using base 2 (binary)
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # perform XOR using ^ operator on integers
    xor = int_a ^ int_b
    
    # convert result back to string using base 2 (binary)
    result = format(xor, 'b')
    
    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
