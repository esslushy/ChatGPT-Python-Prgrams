def choose_num(x: int, y: int) -> int:
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    >>> choose_num(12, 15)
    14
    >>> choose_num(13, 12)
    -1
    """
    max_even = -1
    for num in range(x, y+1):
        if num % 2 == 0 and num > max_even:
            max_even = num
    return max_even

def check(candidate):
    assert candidate(12, 15) == 14
    assert candidate(13, 12) == -1
    assert candidate(33, 12354) == 12354
    assert candidate(5234, 5233) == -1
    assert candidate(6, 29) == 28
    assert candidate(27, 10) == -1
    assert candidate(7, 7) == -1
    assert candidate(546, 546) == 546

def test_check():
    check(choose_num)

test_check()
