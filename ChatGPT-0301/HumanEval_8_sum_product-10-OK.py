from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_of_numbers = sum(numbers)
    product_of_numbers = 1
    for number in numbers:
        product_of_numbers *= number
    return (sum_of_numbers, product_of_numbers)

def check(candidate):
    assert candidate([]) == (0, 1)
    assert candidate([1, 1, 1]) == (3, 1)
    assert candidate([100, 0]) == (100, 0)
    assert candidate([3, 5, 7]) == (15, 105)
    assert candidate([10]) == (10, 10)

def test_check():
    check(sum_product)

test_check()
