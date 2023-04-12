def triangle_area(a: int, b: int, c: int) -> float:
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    >>> triangle_area(3, 4, 5)
    6.0
    >>> triangle_area(1, 2, 10)
    -1
    """
    """
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    >>> triangle_area(3, 4, 5)
    6.0
    >>> triangle_area(1, 2, 10)
    -1
    """
    # Check if the sides form a valid triangle
    if a + b > c and a + c > b and b + c > a:
        # Calculate the semi-perimeter of the triangle
        s = (a + b + c) / 2
        # Calculate the area of the triangle using Heron's formula
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        # Round the area to 2 decimal points and return it
        return round(area, 2)
    else:
        # Return -1 if the sides do not form a valid triangle
        return -1

def check(candidate):
    assert candidate(3, 4, 5) == 6.0
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1
    assert candidate(1, 1, 1) == 0.43
    assert candidate(2, 2, 10) == -1

def test_check():
    check(triangle_area)

test_check()
