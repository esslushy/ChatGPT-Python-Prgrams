def decimal_to_binary(decimal: int) -> str:
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
    >>> decimal_to_binary(15)
    'db1111db'
    >>> decimal_to_binary(32)
    'db100000db'
    """
    binary = bin(decimal)[2:]  # convert decimal to binary string
    return f"db{binary}db"  # add extra characters at the beginning and end

def check(candidate):
    assert candidate(0) == 'db0db'
    assert candidate(32) == 'db100000db'
    assert candidate(103) == 'db1100111db'
    assert candidate(15) == 'db1111db'

def test_check():
    check(decimal_to_binary)

test_check()
