def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    """
    Performs XOR operation on two binary strings.

    Args:
    a: Binary string 1.
    b: Binary string 2.

    Returns:
    A binary string resulting from performing XOR operation between input strings.

    Example:
    string_xor('010', '110') -> '100'
    """
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length.")

    # create an empty list to hold XOR result
    xor_result = []

    # loop through each character of both strings and apply XOR
    for i in range(len(a)):
        if a[i] == b[i]:
            xor_result.append("0")
        else:
            xor_result.append("1")

    # return result as string
    return "".join(xor_result)

def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

def test_check():
    check(string_xor)

test_check()
