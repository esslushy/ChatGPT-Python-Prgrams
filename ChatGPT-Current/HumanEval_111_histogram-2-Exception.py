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
    # Create a dictionary to store the count of each letter
    count_dict = {}
    
    # Split the string into individual letters
    letters = test.split()
    
    # Iterate over each letter and update the count in the dictionary
    for letter in letters:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    # Find the maximum count
    max_count = max(count_dict.values())
    
    # Create a list of letters with the maximum count
    max_letters = [letter for letter, count in count_dict.items() if count == max_count]
    
    # Create a dictionary of the letters with the maximum count and their corresponding count
    result_dict = {letter: count_dict[letter] for letter in max_letters}
    
    return result_dict

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
