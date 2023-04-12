def fib4(n: int) -> int:
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        a, b, c, d = 0, 0, 0, 2
        for i in range(3, n+1):
            a, b, c, d = b, c, d, a+b+c+d
        return d

def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386

def test_check():
    check(fib4)

test_check()
