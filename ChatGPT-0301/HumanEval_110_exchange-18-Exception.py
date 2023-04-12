from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    It is assumed that the input lists will be non-empty.
    """
    # Check if lst1 already contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Find all odd numbers in lst1 and their indices
    odd_nums = [(num, i) for i, num in enumerate(lst1) if num % 2 != 0]
    
    # Find all even numbers in lst2 and their indices
    even_nums = [(num, i) for i, num in enumerate(lst2) if num % 2 == 0]
    
    # If there are not enough even numbers in lst2 to replace all odd numbers in lst1
    if len(even_nums) < len(odd_nums):
        return "NO"
    
    # Sort odd_nums in descending order of their values
    odd_nums.sort(reverse=True)
    
    # Sort even_nums in ascending order of their values
    even_nums.sort()
    
    # Replace odd numbers in lst1 with even numbers from lst2
    for odd_num, odd_index in odd_nums:
        for even_num, even_index in even_nums:
            if even_num > odd_num:
                lst1[odd_index] = even_num
                lst2[even_index] = odd_num
                even_nums.remove((even_num, even_index))
                break
    
    # Check if lst1 now contains only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"

def check(candidate):
    assert candidate([1, 2, 3, 4], [1, 2, 3, 4]) == 'YES'
    assert candidate([1, 2, 3, 4], [1, 5, 3, 4]) == 'NO'
    assert candidate([1, 2, 3, 4], [2, 1, 4, 3]) == 'YES'
    assert candidate([5, 7, 3], [2, 6, 4]) == 'YES'
    assert candidate([5, 7, 3], [2, 6, 3]) == 'NO'
    assert candidate([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == 'NO'
    assert candidate([100, 200], [200, 200]) == 'YES'

def test_check():
    check(exchange)

test_check()
