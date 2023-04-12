from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    >>> compare_one(1, 2.5)
    2.5
    >>> compare_one(1, '2,3')
    '2,3'
    >>> compare_one('5,1', '6')
    '6'
    >>> compare_one('1', 1)
    None
    """
    # Convert strings to floats if they represent real numbers
    if isinstance(a, str):
        a = a.replace(',', '.')
        if '.' in a:
            a = float(a)
        else:
            a = int(a)
    if isinstance(b, str):
        b = b.replace(',', '.')
        if '.' in b:
            b = float(b)
        else:
            b = int(b)
    
    # Compare the values and return the larger one
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

def check(candidate):
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, '2,3') == '2,3'
    assert candidate('5,1', '6') == '6'
    assert candidate('1', '2') == '2'
    assert candidate('1', 1) == None

def test_check():
    check(compare_one)

test_check()
