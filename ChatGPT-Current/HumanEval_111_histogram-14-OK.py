from typing import Dict

def histogram(test: str) -> Dict[str, int]:
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    >>> histogram('a b c')
    { 'a': 1, 'b': 1, 'c': 1 }
    >>> histogram('a b b a')
    { 'a': 2, 'b': 2 }
    >>> histogram('a b c a b')
    { 'a': 2, 'b': 2 }
    >>> histogram('b b b b a')
    { 'b': 4 }
    >>> histogram('')
    {  }

    """
    if not test:
        return {}

    counts = {}
    max_count = 0

    for char in test.split():
        counts[char] = counts.get(char, 0) + 1
        max_count = max(max_count, counts[char])

    result = {}
    for char, count in counts.items():
        if count == max_count:
            result[char] = count

    return result

def check(candidate):
    assert candidate('a b b a') == { 'a': 2, 'b': 2 }
    assert candidate('a b c a b') == { 'a': 2, 'b': 2 }
    assert candidate('a b c d g') == { 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1 }
    assert candidate('r t g') == { 'r': 1, 't': 1, 'g': 1 }
    assert candidate('b b b b a') == { 'b': 4 }
    assert candidate('r t g') == { 'r': 1, 't': 1, 'g': 1 }
    assert candidate('') == {  }
    assert candidate('a') == { 'a': 1 }

def test_check():
    check(histogram)

test_check()
