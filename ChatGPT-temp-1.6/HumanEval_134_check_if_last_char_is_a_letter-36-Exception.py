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
    if not txt:
        return False

    # split the string into words
    words = txt.split()

    # if there is only one word, check if the last character is alphabetical
    if len(words) == 1:
        last_char = words[0][-1]
        return last_char.isalpha() and not last_char.isspace()

    # otherwise, check if the last character of the last word is alphabetical
    else:
        last_word = words[-1]
        last_char = last_word[-1]
        return last_char.isalpha() and last_word[:-1].isalpha() and not last_char.isspace()

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
