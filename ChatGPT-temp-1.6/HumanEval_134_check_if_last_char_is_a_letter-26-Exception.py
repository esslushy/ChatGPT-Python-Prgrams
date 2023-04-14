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
    # If txt is empty string or does not contain a space, return False
    if len(txt) == 0 or ' ' not in txt:
        return False
    
    # Split the txt string based on space and retrieve the last element
    # The strip method is used to remove any whitespaces present
    last_word = txt.split()[-1].strip()

    # Iterate over each character in last_word to check if it is an alphabet or not
    for ch in last_word:
        if not ch.isalpha():
            return False
    
    # If last_word is empty or its length is equal to txt's length, then return False 
    if len(last_word) == 0 or len(last_word) == len(txt):
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
