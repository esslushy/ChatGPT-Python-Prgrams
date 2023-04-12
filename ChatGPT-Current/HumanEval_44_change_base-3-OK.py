def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    if x < 0 or base < 2 or base > 9:
        return ""
    if x == 0:
        return "0"
    result = ""
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result

def check(candidate):
    assert candidate(8, 3) == '22'
    assert candidate(9, 3) == '100'
    assert candidate(234, 2) == '11101010'
    assert candidate(16, 2) == '10000'
    assert candidate(8, 2) == '1000'
    assert candidate(7, 2) == '111'
    assert candidate(2, 3) == '2'
    assert candidate(3, 4) == '3'
    assert candidate(4, 5) == '4'
    assert candidate(5, 6) == '5'
    assert candidate(6, 7) == '6'
    assert candidate(7, 8) == '7'

def test_check():
    check(change_base)

test_check()
