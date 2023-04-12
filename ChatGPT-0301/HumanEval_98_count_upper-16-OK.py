def count_upper(s: str) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    vowels = set('AEIOU')
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels and s[i].isupper():
            count += 1
    return count

def check(candidate):
    assert candidate('aBCdEf') == 1
    assert candidate('abcdefg') == 0
    assert candidate('dBBE') == 0
    assert candidate('B') == 0
    assert candidate('U') == 1
    assert candidate('') == 0
    assert candidate('EEEE') == 2

def test_check():
    check(count_upper)

test_check()
