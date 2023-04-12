def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = ""
    for char in string:
        if char.isupper():
            flipped += char.lower()
        else:
            flipped += char.upper()
    return flipped

def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

def test_check():
    check(flip_case)

test_check()
