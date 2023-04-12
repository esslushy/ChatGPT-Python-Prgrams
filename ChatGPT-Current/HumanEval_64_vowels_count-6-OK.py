def vowels_count(s: str) -> int:
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count('abcde')
    2
    >>> vowels_count('ACEDY')
    3
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    s = s.lower()
    if s[-1] == 'y':
        vowels.append('y')
    for char in s:
        if char in vowels:
            count += 1
    return count

def check(candidate):
    assert candidate('abcde') == 2
    assert candidate('Alone') == 3
    assert candidate('key') == 2
    assert candidate('bye') == 1
    assert candidate('keY') == 2
    assert candidate('bYe') == 1
    assert candidate('ACEDY') == 3

def test_check():
    check(vowels_count)

test_check()
