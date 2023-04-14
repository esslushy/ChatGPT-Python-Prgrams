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
    # We only need to consider one direction, say left to right
    # For each car going left to right, we count the number of cars going
    # right to left that are to its left (i.e. in the opposite lane)
    # These are the potential collisions, since all cars are moving
    # at the same speed and collisions only occur when they meet head-on
    count = 0
    for i in range(n):
        # The number of cars to the left of car i in the opposite lane
        # is simply the same as the index of the car from the right lane
        # that is furthest to the left and to the right of car i in the left lane
        count += i + (n-i-1)
    # We have counted each collision twice, once from the perspective
    # of the left-to-right car, and once from the perspective of the
    # right-to-left car, so we need to divide by 2 to get the total number
    return count // 2

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
