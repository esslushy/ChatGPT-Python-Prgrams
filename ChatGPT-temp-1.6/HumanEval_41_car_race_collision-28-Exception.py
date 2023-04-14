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
    # In each "cycle" of the cars crossing each other,
    # every left-going car will pass every right-going car
    # in front of it; that will result in "n ** 2" potential collisions.
    # However, half of those potential collisions can't happen,
    # because one of the cars is already past the other one.
    # Since the cars are moving at the same speed, we can consider
    # the reference frame of a single right-going car and analyze
    # the positions and speeds of the left-going cars as seen by
    # this car. The collisions with this car will occur exactly
    # when a left-going car has started to pass it and has not
    # finished doing so. For such a left-going car, its speed and
    # position relative to the right-going car determine when this
    # will happen, so we just need to go through all possible
    # such combinations of left- and right-going cars to find
    # out which ones collide.
    
    # Compute the time needed for any left-going car to reach
    # any right-going car that starts from a specific distance.
    def collision_time(left_pos, right_pos):
        return (left_pos + right_pos) / 2
        
    collisions = 0
    
    for right_pos in range(n):
        for left_pos in range(n):
            if left_pos != right_pos:
                t = collision_time(left_pos, n - 1 - right_pos)
                if t < n:
                    # A collision will occur only if the cars are not
                    # already separated by more than "n" units at that
                    # point in time, meaning that the time computed
                    # must be less than "n". We can safely round down
                    # the result, as we know the time is never an
                    # exact fraction of the total length of the road.
                    if int(t) == t:
                        collisions += 1
    
    # We count the total number of collisions, and each of them
    # contributes two cars, so we need to divide by 2.
    return collisions // 2

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
