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
    # we can count collisions by calculating the number of pairs of cars
    # moving towards each other
    # each car going left-to-right is colliding with the closest car
    # moving right-to-left, that is, the one that started out ahead of it
    # similarly, each car going right-to-left is colliding with the closest
    # car moving left-to-right, that is, the one that started out ahead of it
    # since we assume all cars are moving at the same speed, the relative
    # position of each pair of cars is not changing, so there can only be one
    # collision per pair of cars
    return n * (n - 1) // 2

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
