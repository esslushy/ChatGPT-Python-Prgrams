def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()
    
    # Create an empty set to store distinct characters
    distinct_chars = set()
    
    # Iterate over each character in the string
    for char in string:
        # Add the character to the set if it's not already in there
        if char not in distinct_chars:
            distinct_chars.add(char)
    
    # Return the length of the set, which is the number of distinct characters
    return len(distinct_chars)

def check(candidate):
    assert candidate('') == 0
    assert candidate('abcde') == 5
    assert candidate('abcdecadeCADE') == 5
    assert candidate('aaaaAAAAaaaa') == 1
    assert candidate('Jerry jERRY JeRRRY') == 5

def test_check():
    check(count_distinct_characters)

test_check()
