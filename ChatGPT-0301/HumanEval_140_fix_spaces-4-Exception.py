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
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace consecutive spaces with hyphen
    i = 0
    while i < len(text):
        if text[i] == " ":
            count = 1
            for j in range(i+1, len(text)):
                if text[j] == " ":
                    count += 1
                else:
                    break
            if count > 2:
                text = text[:i] + "-" + text[i+count:]
            i += count
        else:
            i += 1
    
    return text.strip("-")

def check(candidate):
    assert candidate('Example') == 'Example'
    assert candidate('Mudasir Hanif ') == 'Mudasir_Hanif_'
    assert candidate('Yellow Yellow  Dirty  Fellow') == 'Yellow_Yellow__Dirty__Fellow'
    assert candidate('Exa   mple') == 'Exa-mple'
    assert candidate('   Exa 1 2 2 mple') == '-Exa_1_2_2_mple'

def test_check():
    check(fix_spaces)

test_check()
