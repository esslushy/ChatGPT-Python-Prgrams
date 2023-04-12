def fix_spaces(text: str) -> str:
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    >>> fix_spaces(' Example')
    'Example'
    >>> fix_spaces(' Example 1')
    'Example_1'
    >>> fix_spaces(' Example 2')
    '_Example_2'
    >>> fix_spaces(' Example 3')
    '_Example-3'
    """
    text = text.strip()  # remove leading and trailing spaces
    if '  ' in text:  # check if there are consecutive spaces
        text = text.replace('  ', '-')  # replace consecutive spaces with -
    text = text.replace(' ', '_')  # replace remaining spaces with _
    return text

def check(candidate):
    assert candidate('Example') == 'Example'
    assert candidate('Mudasir Hanif ') == 'Mudasir_Hanif_'
    assert candidate('Yellow Yellow  Dirty  Fellow') == 'Yellow_Yellow__Dirty__Fellow'
    assert candidate('Exa   mple') == 'Exa-mple'
    assert candidate('   Exa 1 2 2 mple') == '-Exa_1_2_2_mple'

def test_check():
    check(fix_spaces)

test_check()
