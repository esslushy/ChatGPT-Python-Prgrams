def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """
    Perform binary XOR on two strings of equal length.

    Parameters:
    a (str): First input string consisting only of 1s and 0s.
    b (str): Second input string consisting only of 1s and 0s.
    
    Returns:
    str: Result of the XOR operation also as a string consisting of 1s and 0s.

    Examples:
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('0011', '1010')
    '1001'
    """

    # Make sure the two input strings have the same length
    assert len(a) == len(b), "Inputs must be of the same length"

    result = ""
    # Perform XOR operation bit by bit
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
