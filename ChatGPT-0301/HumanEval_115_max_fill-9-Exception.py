from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
    >>> max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1)
    6

    Example 2:
    >>> max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2)
    5
    
    Example 3:
    >>> max_fill([[0, 0, 0], [0, 0, 0]], 5)
    0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    # Initialize variables
    num_buckets = 0
    total_water = 0
    
    # Iterate over each well in the grid
    for well in grid:
        # Calculate the amount of water in the well
        well_water = sum(well)
        
        # If the well is empty, move on to the next well
        if well_water == 0:
            continue
        
        # Calculate the number of buckets needed to empty the well
        buckets_needed = well_water // capacity
        if well_water % capacity != 0:
            buckets_needed += 1
        
        # Add the number of buckets needed to the total
        num_buckets += buckets_needed
        
        # Add the amount of water in the well to the total
        total_water += well_water
    
    # Calculate the number of times the buckets need to be lowered
   
def check(candidate):
    assert candidate([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert candidate([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert candidate([[0, 0, 0], [0, 0, 0]], 5) == 0
    assert candidate([[1, 1, 1, 1], [1, 1, 1, 1]], 2) == 4
    assert candidate([[1, 1, 1, 1], [1, 1, 1, 1]], 9) == 2

def test_check():
    check(max_fill)

test_check()
