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
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    """
    if not test:
        return {}

    # Split the string into a list of words
    words = test.split()

    # Create a dictionary to store the count of each letter
    count = {}

    # Loop through each word and count the occurrence of each letter
    for word in words:
        for letter in word:
            count[letter] = count.get(letter, 0) + 1

    # Find the maximum count
    max_count = max(count.values())

    # Create a list of letters with the maximum count
    result = [letter for letter, count in count.items() if count == max_count]

    # Create a dictionary with the result
    return {letter: count[letter] for letter in result}

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
