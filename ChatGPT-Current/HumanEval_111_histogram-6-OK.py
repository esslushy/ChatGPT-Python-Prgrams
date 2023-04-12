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

    # Loop through each word in the list
    for word in words:
        # Loop through each letter in the word
        for letter in word:
            # Increment the count of the letter in the dictionary
            count[letter] = count.get(letter, 0) + 1

    # Find the maximum count of any letter
    max_count = max(count.values())

    # Create a list of letters that have the maximum count
    result = {letter: count[letter] for letter in count if count[letter] == max_count}

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
