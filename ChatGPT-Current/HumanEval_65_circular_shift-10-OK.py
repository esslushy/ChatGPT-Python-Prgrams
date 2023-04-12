def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    '21'
    >>> circular_shift(12, 2)
    '12'
    """
    x_str = str(x)
    n = len(x_str)
    if shift > n:
        return x_str[::-1]
    else:
        shifted_str = x_str[-shift:] + x_str[:-shift]
        return shifted_str

def check(candidate):
    assert candidate(100, 2) == '001'
    assert candidate(12, 2) == '12'
    assert candidate(97, 8) == '79'
    assert candidate(12, 1) == '21'
    assert candidate(11, 101) == '11'

def test_check():
    check(circular_shift)

test_check()
