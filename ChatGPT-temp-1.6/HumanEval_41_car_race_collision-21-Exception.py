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
    # We can model this problem as a pair of races with the same n cars, each one driving at the same speed
    # and the same direction. We only need to count the number of colliding pairs for each car of one
    # direction with cars of the other direction (there will be n * n pairs to check).
    
    # Each car starts at some arbitrary position, say 0 or a big negative number, and it will move to
    # the right or to the left. Therefore, each car is defined by a tuple (position, direction), where
    # direction is either 1 for rightwards, or -1 for leftwards.

    # Here, we define a helper function that returns the initial position and direction for each car
    def car_start(i):
        if i < n:
            return (-i - 1, 1)  # Rightwards cars start at -1 and move towards positive values
        else:
            return (i - n, -1)  # Leftwards cars start at n-1 and move towards negative values

    # We initialize the cars array as a list of (position, direction) tuples, one for each car
    cars = [car_start(i) for i in range(2 * n)]

    # We will use two pointer algorithms, one for each direction.
    cars_right, cars_left = sorted(cars[:n]), sorted(cars[n:])

    # Initialize counter for number of collisions
    num_collisions = 0

    # We can iterate on both lists using two pointers for each direction
    r, l = 0, 0
    while r < n and l < n:
        pos_r, dir_r = cars_right[r]
        pos_l, dir_l = cars_left[l]
        if pos_r <= pos_l:  # There is a collision
            num_collisions += 1
            r += 1
        else:
            l += 1

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
