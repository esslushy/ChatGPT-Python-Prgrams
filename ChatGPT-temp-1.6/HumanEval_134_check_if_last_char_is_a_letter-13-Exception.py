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
    """
    Returns True if the last character of a given string is an
    alphabetical character and is not a part of a word, False otherwise.
    Note: "word" is a group of characters separated by space.
    """
    if not txt or txt[-1].isdigit():
        # Return False if string is empty or the last character is a digit
        return False
    
    txt_split = txt.strip().split()  # split the string into words
    if len(txt_split) == 0:
        # Return False if the stripped string has no words
        return False
    
    # Check if last character is an alphabet and not part of last word
    last_word = txt_split[-1] 
    return txt[-1].isalpha() and txt[-1] not in last_word

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
