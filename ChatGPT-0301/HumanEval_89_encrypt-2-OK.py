def encrypt(s: str) -> str:
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    >>> encrypt('hi')
    'lm'
    >>> encrypt('asdfghjkl')
    'ewhjklnop'
    >>> encrypt('gf')
    'kj'
    >>> encrypt('et')
    'ix'
    """
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    """
    result = ""
    for char in s:
        if char.isalpha():
            shifted = chr((ord(char) - 97 + 2 * 2) % 26 + 97)
            result += shifted
        else:
            result += char
    return result

def check(candidate):
    assert candidate('hi') == 'lm'
    assert candidate('asdfghjkl') == 'ewhjklnop'
    assert candidate('gf') == 'kj'
    assert candidate('et') == 'ix'
    assert candidate('faewfawefaewg') == 'jeiajeaijeiak'
    assert candidate('hellomyfriend') == 'lippsqcjvmirh'
    assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh') == 'hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl'
    assert candidate('a') == 'e'

def test_check():
    check(encrypt)

test_check()
