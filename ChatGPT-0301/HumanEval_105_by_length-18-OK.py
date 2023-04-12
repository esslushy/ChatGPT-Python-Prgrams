from typing import List

def by_length(arr: List[int]) -> List[str]:
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
    >>> by_length([2, 1, 1, 4, 5, 8, 2, 3])
    ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    
      If the array is empty, return an empty array:
    >>> by_length([])
    []
    
      If the array has any strange number ignore it:
    >>> by_length([1, -1, 55])
    ['One']
    """
    digit_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(filtered_arr, reverse=True)
    return [digit_names[x] for x in sorted_arr]

def check(candidate):
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
    assert candidate([]) == []
    assert candidate([1, -1, 55]) == ['One']
    assert candidate([1, -1, 3, 2]) == ['Three', 'Two', 'One']
    assert candidate([9, 4, 8]) == ['Nine', 'Eight', 'Four']

def test_check():
    check(by_length)

test_check()
