from typing import List

def select_words(s: str, n: int) -> List[str]:
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    >>> select_words('Mary had a little lamb', 4)
    ['little']
    >>> select_words('Mary had a little lamb', 3)
    ['Mary', 'lamb']
    >>> select_words('simple white space', 2)
    []
    >>> select_words('Hello world', 4)
    ['world']
    >>> select_words('Uncle sam', 3)
    ['Uncle']
    """
    # Create a list of consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    
    # Split the string into words
    words = s.split()
    
    # Create an empty list to store the words that meet the criteria
    selected_words = []
    
    # Iterate over each word
    for word in words:
        # Count the number of consonants in the word
        num_consonants = sum([1 for letter in word if letter.lower() in consonants])
        
        # If the number of consonants in the word is equal to n, add it to the selected_words list
        if num_consonants == n:
            selected_words.append(word)
    
    return selected_words

def check(candidate):
    assert candidate('Mary had a little lamb', 4) == ['little']
    assert candidate('Mary had a little lamb', 3) == ['Mary', 'lamb']
    assert candidate('simple white space', 2) == []
    assert candidate('Hello world', 4) == ['world']
    assert candidate('Uncle sam', 3) == ['Uncle']
    assert candidate('', 4) == []
    assert candidate('a b c d e f', 1) == ['b', 'c', 'd', 'f']

def test_check():
    check(select_words)

test_check()
