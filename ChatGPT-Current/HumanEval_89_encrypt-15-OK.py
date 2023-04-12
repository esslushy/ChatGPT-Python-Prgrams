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
    shift = 2 * 2
    result = ''
    for char in s:
        if char.isalpha():
            char_code = ord(char) + shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            else:
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            result += chr(char_code)
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
