def car_race_collision(n: int) -> int:
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # If there are less than two cars on each side, no collisions are possible
    if n < 2:
        return 0
    
    # Assuming all cars have same speed and starting distance, we can
    # calculate the time to collision for each car using simple math
    time_to_collision = [2*i/(n+1) for i in range(1, n+1)]
    
    # We can then count the number of collisions by counting the number of
    # intersections between the left-to-right and right-to-left cars' paths.
    # Since each car has a unique time to collision, sorting the lists by this
    # value allows us to efficiently identify these intersections.
    left_to_right = sorted(time_to_collision)
    right_to_left = sorted(time_to_collision, reverse=True)
    
    collisions = 0
    # Starting index for each car in the opposite direction's list
    j = 0
    for i in range(n):
        while j < n and right_to_left[j] < left_to_right[i]:
            j += 1
        collisions += j
    return collisions

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
