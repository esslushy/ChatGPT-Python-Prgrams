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
    # Each car on one side of the road will eventually pass each car on the other side.
    # We don't care about collisions that happen between cars that have already passed each other.
    # Therefore, we only need to count collisions that happen between a car on the left
    # and a car on the right if they meet head-on. In other words, if we order the cars
    # on each side by their starting positions, the cars that collide will be at positions
    # 0 and n-1, 1 and n-2, 2 and n-3, and so on. There will be n//2 such pairs.

    return n // 2

def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
