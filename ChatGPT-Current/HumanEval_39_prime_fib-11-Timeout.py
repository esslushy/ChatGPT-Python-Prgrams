def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize the first two Fibonacci numbers
    fib1, fib2 = 1, 1
    count = 2

    while True:
        # Generate the next Fibonacci number
        fib = fib1 + fib2
        count += 1

        # Check if the Fibonacci number is prime
        if is_prime(fib):
            # If we've found the nth prime Fibonacci number, return it
            if count == n:
                return fib
        # Update the Fibonacci numbers for the next iteration
        fib1, fib2 = fib2, fib

def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437

def test_check():
    check(prime_fib)

test_check()
