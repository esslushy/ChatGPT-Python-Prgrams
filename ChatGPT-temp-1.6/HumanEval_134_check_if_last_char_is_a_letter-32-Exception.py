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
    Returns True if the last character of a given string is
    an alphabetical character and is not part of a word, False
    otherwise.
    """
    if not txt or txt[-1] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return False

    # If last character is a letter, check if it is part of a word.
    if ' ' in txt[:-1]:
        if not txt[txt.rindex(' ')+1:-1].isalpha():
            return True

    # If no spaces in txt or if last character is not part of a word, return True.
    else:
        return True

    return False

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
