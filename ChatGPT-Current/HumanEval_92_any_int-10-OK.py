def any_int(x: float, y: float, z: float) -> bool:
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    >>> any_int(5, 2, 7)
    True
    
    >>> any_int(3, 2, 2)
    False

    >>> any_int(3, -2, 1)
    True
    
    >>> any_int(3.6, -2.2, 2)
    False
  

    
    """
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    return any(i == j + k or j == i + k or k == i + j for i, j, k in [(x, y, z), (y, x, z), (z, x, y)])

def check(candidate):
    assert candidate(2, 3, 1) == True
    assert candidate(2.5, 2, 3) == False
    assert candidate(1.5, 5, 3.5) == False
    assert candidate(2, 6, 2) == False
    assert candidate(4, 2, 2) == True
    assert candidate(2.2, 2.2, 2.2) == False
    assert candidate(-4, 6, 2) == True
    assert candidate(2, 1, 1) == True
    assert candidate(3, 4, 7) == True
    assert candidate(3.0, 4, 7) == False

def test_check():
    check(any_int)

test_check()
