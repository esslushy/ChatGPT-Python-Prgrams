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

    # A collision occurs when a left-moving car overtakes a right-moving car,
    # i.e. when its distance from the left edge is less than the right-moving
    # car's distance from the right edge.
    # The number of collisions is thus equal to the number of times a left-moving car
    # overtakes a right-moving car.

    # Let's calculate the positions of the cars when they collide.
    # Since both sets of cars start far away from each other, we can imagine that
    # the left-moving cars start at position 0 and the right-moving cars start
    # at position 2*n-1, and they meet at position n.

    # We can thus consider the problem as follows:
    # Imagine we have n points randomly arranged on the interval [0,2*n-1],
    # and we want to count the number of inversions between those points.
    # That is, how many pairs of points (i,j) are there where i < j but x_i > x_j?

    # We can solve this problem by using merge sort.

    arr = list(range(2 * n)) # A list of numbers from 0 to 2*n-1.
    # Shuffle the list.
    # We need to shuffle the list because if the left-moving cars always start
    # at the leftmost positions and the right-moving cars always start at the
    # rightmost positions, the number of inversions will be 0.
    random.shuffle(arr)

    # Define a merge function to merge two sorted lists and count the number of inversions.
    def merge(arr, lo, mid, hi):
        i, j =
def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100

def test_check():
    check(car_race_collision)

test_check()
