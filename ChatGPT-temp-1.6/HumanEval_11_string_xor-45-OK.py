def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """Performs binary XOR operation on two binary strings."""
    result = ""
    for i in range(min(len(a), len(b))):
        result += "1" if a[i] != b[i] else "0"
    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
