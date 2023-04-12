from typing import List

def count_up_to(n: int) -> List[int]:
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    >>> count_up_to(5)
    [2, 3]
    >>> count_up_to(11)
    [2, 3, 5, 7]
    >>> count_up_to(0)
    []
    >>> count_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> count_up_to(1)
    []
    >>> count_up_to(18)
    [2, 3, 5, 7, 11, 13, 17]
    """
    if n < 2:
        return []
    
    primes = [2]
    for num in range(3, n):
        is_prime = True
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes

def check(candidate):
    assert candidate(5) == [2, 3]
    assert candidate(6) == [2, 3, 5]
    assert candidate(7) == [2, 3, 5]
    assert candidate(10) == [2, 3, 5, 7]
    assert candidate(0) == []
    assert candidate(22) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert candidate(1) == []
    assert candidate(18) == [2, 3, 5, 7, 11, 13, 17]
    assert candidate(47) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    assert candidate(101) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def test_check():
    check(count_up_to)

test_check()
