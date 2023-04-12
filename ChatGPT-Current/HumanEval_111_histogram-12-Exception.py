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
    # Create an empty dictionary to store the count of each letter
    count = {}
    
    # Split the string into a list of words
    words = test.split()
    
    # Loop through each word in the list
    for word in words:
        # Loop through each letter in the word
        for letter in word:
            # If the letter is already in the dictionary, increment its count
            if letter in count:
                count[letter] += 1
            # Otherwise, add the letter to the dictionary with a count of 1
            else:
                count[letter] = 1
    
    # Find the maximum count of any letter in the dictionary
    max_count = max(count.values())
    
    # Create a new dictionary to store the letters with the maximum count
    result = {}
    
    # Loop through each letter in the dictionary
    for letter, count in count.items():
        # If the count of the letter is equal to the maximum count, add it to the result dictionary
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
