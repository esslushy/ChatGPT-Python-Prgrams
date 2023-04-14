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
    if len(txt) == 0:     # checking if string is empty
        return False
    else:
        txt_list = txt.split()    # splitting the string by space to create a list of words
        last_word = txt_list[-1]  # taking the last word from the list
        last_char = last_word[-1]  # taking the last character from the last word
        
        if last_char.isalpha() and last_word == txt.strip().split()[-1]:
            # checking if last character is an alphabetical character and if the last word is not a part of another word
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
