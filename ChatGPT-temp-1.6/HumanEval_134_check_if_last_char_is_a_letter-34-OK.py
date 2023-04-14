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
    Returns True if the last character of the string is an
    alphabetical character and is not part of a word.

    Args:
    - txt: A string.

    Returns:
    - A boolean value.

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
    if len(txt) == 0:
        return False
    elif txt[-1].isalpha() and (len(txt) == 1 or not txt[-2].isalpha()):
        return True
    else:
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
