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
    # All cars move in the same speed, so we don't really care about the speed
    # Let's assume the position of the cars as distance from a common starting point
    # The first n positions represent the positions of the left-to-right cars,
    # sorted in increasing order. The next n positions represent the positions
    # of the right-to-left cars, also sorted in increasing order.

    positions = [0] * (2 * n)

    # We generate n random positions for the left-to-right cars, and make
    # sure they are sorted. We do the same for the right-to-left cars, but
    # we add a very large value to each position so they appear in reverse order
    # with respect to the left-to-right cars.
    import random
    for i in range(n):
        positions[i] = random.random()
    positions[:n] = sorted(positions[:n])
    for i in range(n):
        positions[n + i] = 1e6 + random.random()
    positions[n:] = sorted(positions[n:], reverse=True)

    # We iterate over all the cars, and every time we find a right-to-left car
    # that is located before a left-to-right car, we count a collision.
    count = 0
    for i in range(1, 2 * n):
        if positions[i-1] <= positions[i-n] <= positions[i]:
            count += 1

    return count

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
