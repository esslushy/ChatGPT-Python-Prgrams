from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + 2*i)
        else:
            stones.append(n + 2*i - 1)
    return stones

def check(candidate):
    assert candidate(3) == [3, 5, 7]
    assert candidate(4) == [4, 6, 8, 10]
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

def test_check():
    check(make_a_pile)

test_check()
