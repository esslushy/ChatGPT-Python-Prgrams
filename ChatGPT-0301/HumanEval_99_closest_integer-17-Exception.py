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
    # Convert the string value to a float
    f_value = float(value)

    # Check if the float value is already an integer
    if f_value.is_integer():
        return int(f_value)

    # Calculate the distance to the nearest lower and upper integers
    lower_dist = f_value - int(f_value)
    upper_dist = 1 - lower_dist

    # Round away from zero
    if lower_dist < upper_dist:
        return int(f_value)
    else:
        return int(f_value) + 1 if f_value > 0 else int(f_value) - 1

def check(candidate):
    assert candidate('10') == 10
    assert candidate('14.5') == 15
    assert candidate('-15.5') == -16
    assert candidate('15.3') == 15
    assert candidate('0') == 0

def test_check():
    check(closest_integer)

test_check()
