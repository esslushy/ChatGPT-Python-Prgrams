def closest_integer(value: str) -> int:
    """
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer('10')
    10
    >>> closest_integer('15.3')
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    """
    # Convert the input string to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # If the number is positive, round up to the nearest integer
    if num > 0:
        return int(num + 0.5)

    # If the number is negative, round down to the nearest integer
    if num < 0:
        return int(num - 0.5)

def check(candidate):
    assert candidate('10') == 10
    assert candidate('14.5') == 15
    assert candidate('-15.5') == -16
    assert candidate('15.3') == 15
    assert candidate('0') == 0

def test_check():
    check(closest_integer)

test_check()
