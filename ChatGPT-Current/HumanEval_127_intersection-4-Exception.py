from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    >>> intersection((1, 2), (2, 3))
    'NO'
    >>> intersection((-1, 1), (0, 4))
    'NO'
    >>> intersection((-3, -1), (-5, 5))
    'YES'
    """
    start1, end1 = interval1
    start2, end2 = interval2

    # Check if the intervals intersect
    if end1 < start2 or end2 < start1:
        return "NO"

    # Calculate the length of the intersection
    intersection_start = max(start1, start2)
    intersection_end = min(end1, end2)
    intersection_length = intersection_end - intersection_start + 1

    # Check if the length of the intersection is a prime number
    if intersection_length < 2:
        return "NO"
    for i in range(2, int(intersection_length ** 0.5) + 1):
        if intersection_length % i == 0:
            return "NO"
    return "YES"

def check(candidate):
    assert candidate((1, 2), (2, 3)) == 'NO'
    assert candidate((-1, 1), (0, 4)) == 'NO'
    assert candidate((-3, -1), (-5, 5)) == 'YES'
    assert candidate((-2, 2), (-4, 0)) == 'YES'
    assert candidate((-11, 2), (-1, -1)) == 'NO'
    assert candidate((1, 2), (3, 5)) == 'NO'
    assert candidate((1, 2), (1, 2)) == 'NO'
    assert candidate((-2, -2), (-3, -2)) == 'NO'

def test_check():
    check(intersection)

test_check()
