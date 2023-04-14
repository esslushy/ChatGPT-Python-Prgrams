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
    if len(txt) == 0:  # empty string
        return False

    txt = txt.strip()  # remove any white spaces at the end
    words = txt.split()  # split the string into a list of words

    if len(words) == 0:  # if there are no words
        return False

    last_word = words[-1]  # get the last word

    if len(last_word) == 0:  # if the last word is empty
        return False

    last_char = last_word[-1]  # get the last character of the last word

    if not last_char.isalpha():  # if the last character is not an alphabet
        return False

    if len(last_word) == 1:  # if the last word is a single letter
        return True

    second_last_char = last_word[-2]  # get the second last character of the last word

    if second_last_char == " ":  # if the last character is not a part of a word
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
