from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    if not nums:
        return 0
    
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        current_sum = max(current_sum, 0)
        
    return min_sum

def check(candidate):
    assert candidate([2, 3, 4, 1, 2, 4]) == 1
    assert candidate([-1, -2, -3]) == -6
    assert candidate([-1, -2, -3, 2, -10]) == -14
    assert candidate([-9999999999999999]) == -9999999999999999
    assert candidate([0, 10, 20, 1000000]) == 0
    assert candidate([-1, -2, -3, 10, -5]) == -6
    assert candidate([100, -1, -2, -3, 10, -5]) == -6
    assert candidate([10, 11, 13, 8, 3, 4]) == 3
    assert candidate([100, -33, 32, -1, 0, -2]) == -33
    assert candidate([-10]) == -10
    assert candidate([7]) == 7
    assert candidate([1, -1]) == -1

def test_check():
    check(minSubArraySum)

test_check()
