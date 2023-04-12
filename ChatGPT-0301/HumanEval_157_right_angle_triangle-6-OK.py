def right_angle_triangle(a: int, b: int, c: int) -> bool:
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    >>> right_angle_triangle(3, 4, 5)
    True
    >>> right_angle_triangle(1, 2, 3)
    False
    """
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    # Check if the Pythagorean theorem holds
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def check(candidate):
    assert candidate(3, 4, 5) == True
    assert candidate(1, 2, 3) == False
    assert candidate(10, 6, 8) == True
    assert candidate(2, 2, 2) == False
    assert candidate(7, 24, 25) == True
    assert candidate(10, 5, 7) == False
    assert candidate(5, 12, 13) == True
    assert candidate(15, 8, 17) == True
    assert candidate(48, 55, 73) == True
    assert candidate(1, 1, 1) == False
    assert candidate(2, 2, 10) == False

def test_check():
    check(right_angle_triangle)

test_check()
