from typing import List

def sort_third(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    # Create a list of indices that are divisible by 3
    indices = [i for i in range(len(l)) if i % 3 == 0]
    # Create a list of values at those indices
    values = [l[i] for i in indices]
    # Sort the values
    values.sort()
    # Create a new list with the sorted values at the divisible-by-3 indices
    result = [values.pop(0) if i in indices else l[i] for i in range(len(l))]
    return result

def check(candidate):
    assert candidate([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert candidate([5, 8, 3, 4, 6, 9, 2]) == [2, 8, 3, 4, 6, 9, 5]
    assert candidate([5, 6, 9, 4, 8, 3, 2]) == [2, 6, 9, 4, 8, 3, 5]
    assert candidate([5, 6, 3, 4, 8, 9, 2, 1]) == [2, 6, 3, 4, 8, 9, 5, 1]

def test_check():
    check(sort_third)

test_check()
