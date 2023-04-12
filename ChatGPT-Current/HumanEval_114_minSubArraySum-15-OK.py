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
    """
    # Initialize variables to keep track of the minimum sum and current sum
    min_sum = float('inf')
    curr_sum = 0
    
    # Iterate through the array
    for num in nums:
        # Add the current number to the current sum
        curr_sum += num
        
        # If the current sum is less than the minimum sum, update the minimum sum
        if curr_sum < min_sum:
            min_sum = curr_sum
        
        # If the current sum is greater than or equal to zero, reset the current sum
        if curr_sum >= 0:
            curr_sum = 0
    
    # Return the minimum sum
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
