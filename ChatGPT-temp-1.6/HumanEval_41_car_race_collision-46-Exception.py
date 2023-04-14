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
    # initialize the number of collisions to zero
    collisions = 0
    
    # simulate the movement of the cars
    for i in range(n):
        # calculate the positions of the left-moving and right-moving cars at time i
        left_pos = i
        right_pos = n + i
        
        # check if the left-moving car and the right-moving car collide at time i
        if left_pos == right_pos:
            collisions += 1
    
    # return the number of collisions
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
