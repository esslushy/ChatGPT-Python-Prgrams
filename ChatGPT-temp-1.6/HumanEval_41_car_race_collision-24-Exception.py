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
    left_cars = sorted(range(n))
    right_cars = sorted(range(n), reverse=True)
    
    i = 0 # pointer for left_cars
    j = 0 # pointer for right_cars
    num_collisions = 0
    
    while i < n and j < n:
        if left_cars[i] < right_cars[j]:
            # left_cars[i] cannot collide with any remaining right_cars
            i += 1
        else:
            # left_cars[i] can collide with all remaining right_cars
            num_collisions += n - j
            j += 1
       
    return num_collisions

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
