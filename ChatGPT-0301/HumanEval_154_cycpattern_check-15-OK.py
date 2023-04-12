def cycpattern_check(a: str, b: str) -> bool:
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    >>> cycpattern_check('abcd', 'abd')
    False
    >>> cycpattern_check('hello', 'ell')
    True
    >>> cycpattern_check('whassup', 'psus')
    False
    >>> cycpattern_check('abab', 'baa')
    True
    >>> cycpattern_check('efef', 'eeff')
    False
    >>> cycpattern_check('himenss', 'simen')
    True

    """
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    """
    if len(a) < len(b):
        return False
    
    for i in range(len(b)):
        if b in a:
            return True
        b = b[1:] + b[0]
    
    return False

def check(candidate):
    assert candidate('xyzw', 'xyw') == False
    assert candidate('yello', 'ell') == True
    assert candidate('whattup', 'ptut') == False
    assert candidate('efef', 'fee') == True
    assert candidate('abab', 'aabb') == False
    assert candidate('winemtt', 'tinem') == True

def test_check():
    check(cycpattern_check)

test_check()
