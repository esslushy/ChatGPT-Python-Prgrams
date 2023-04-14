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
    # Remove trailing white spaces from the text
    txt = txt.rstrip()

    # Split the string by spaces and check the last chunk
    # to see if it's an alphabetical character.
    chunks = txt.split()
    if chunks:
        last_chunk = chunks[-1]
        if last_chunk.isalpha():
            # Check if it's the only chunk.
            if len(chunks) == 1:
                return True
            else:
                # Check if it's separated by a space from the other chunks.
                if txt[-len(last_chunk)-1] == ' ':
                    return True
    
    # If none of the conditions above is satisfied, return False.
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
