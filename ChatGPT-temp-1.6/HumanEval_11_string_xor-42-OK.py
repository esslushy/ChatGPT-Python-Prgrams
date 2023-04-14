def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """ Perform binary XOR on input strings a and b and return result.
    Both input strings are assumed to consist only of 1s and 0s.
    Returns a string.
    """
    result = ''
    for char_a, char_b in zip(a, b):
        if char_a != char_b:
            result += '1'
        else:
            result += '0'
    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
