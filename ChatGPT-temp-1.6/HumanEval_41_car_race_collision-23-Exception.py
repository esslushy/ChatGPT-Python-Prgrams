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
    # We can assume that the cars are initially arranged in any pattern, because
    # they will always sort themselves out before any collision can happen.
    # So we can simply consider a "slice" of the cars that is going from
    # right-to-left, and a "slice" that is going from left-to-right. The slices
    # will be ordered in opposite directions, which makes the collision detection
    # easy.

    # We can start by computing the time that it would take for two cars on
    # opposite sides to collide. Since they are moving towards each other at
    # the same speed, this happens when they are exactly n cars apart from
    # each other (assuming the cars are of length 1).

    # Note: We only need to compute the collision times for the cars in the
    # right-to-left slice, since those are the ones that can collide with the
    # left-to-right cars. The left-to-right slice will always come in the order
    # 1, 2, ..., n, so we don't need to compute any collision times for those
    # cars.

    # For the right-to-left cars, we can store their current position and their
    # collision time in a tuple.
    collision_times = [(i + 1 + n, (i + 1 + n) / n) for i in range(n)]

    # Then, we can sort this list of tuples by collision time, so that we can
    # iterate through it and detect collisions in order.
    collision_times.sort(key=lambda x: x[1])

    # Now we can iterate through the collision times
def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
