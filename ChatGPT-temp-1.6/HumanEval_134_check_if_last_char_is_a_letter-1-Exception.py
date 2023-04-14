def check_if_last_char_is_a_letter(txt: str) -> bool:
    """
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    >>> check_if_last_char_is_a_letter('apple pie')
    False
    >>> check_if_last_char_is_a_letter('apple pi e')
    True
    >>> check_if_last_char_is_a_letter('apple pi e ')
    False
    >>> check_if_last_char_is_a_letter('')
    False
    """
    # Remove the trailing whitespaces and split the words
    words = txt.strip().split()
    
    # Return False if no words found or last character is not alphabetic
    if len(words) == 0 or not words[-1][-1].isalpha():
        return False
    
    # Check if last character is not part of a word
    for i in range(len(words)-1):
        if words[i][-1].isalpha():
            return False
    
    return True

def check(candidate):
    assert candidate('apple') == False
    assert candidate('apple pi e') == True
    assert candidate('eeeee') == False
    assert candidate('A') == True
    assert candidate('Pumpkin pie ') == False
    assert candidate('Pumpkin pie 1') == False
    assert candidate('') == False
    assert candidate('eeeee e ') == False
    assert candidate('apple pie') == False
    assert candidate('apple pi e ') == False

def test_check():
    check(check_if_last_char_is_a_letter)

test_check()
