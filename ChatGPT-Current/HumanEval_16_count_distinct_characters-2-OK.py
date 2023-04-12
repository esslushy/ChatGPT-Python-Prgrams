def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case
    string = string.lower()
    
    # Use a set to store unique characters
    unique_chars = set(string)
    
    # Return the length of the set
    return len(unique_chars)

def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcdecadeCADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5

def test_check():
    check(count_distinct_characters)

test_check()
