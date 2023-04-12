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
    # Create an empty dictionary to store the counts of each letter
    counts = {}

    # Split the input string into a list of lowercase letters
    letters = test.lower().split()

    # Loop through each letter and increment its count in the dictionary
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Find the maximum count
    max_count = max(counts.values())

    # Create a new dictionary to store the letters with the maximum count
    result = {}
    for letter, count in counts.items():
        if count == max_count:
            result[letter] = count

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
