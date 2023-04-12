from typing import List

def sort_even(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = sorted(even_values)
    result = [l[i] if i % 2 == 1 else sorted_even_values.pop(0) for i in range(len(l))]
    return result

def check(candidate):
    assert candidate([1, 2, 3]) == [1, 2, 3]
    assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]
    assert candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]) == [-12, 8, 3, 4, 5, 2, 12, 11, 23, -10]

def test_check():
    check(sort_even)

test_check()
