from typing import Dict

def check_dict_case(dict: Dict[str, str]) -> bool:
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    >>> check_dict_case({ 'a': 'apple', 'b': 'banana' })
    True
    >>> check_dict_case({ 'a': 'apple', 'A': 'banana', 'B': 'banana' })
    False
    >>> check_dict_case({ 'a': 'apple', 8: 'banana', 'a': 'apple' })
    False
    >>> check_dict_case({ 'Name': 'John', 'Age': '36', 'City': 'Houston' })
    False
    >>> check_dict_case({ 'STATE': 'NC', 'ZIP': '12345' })
    True
    """
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    """
    if not dict:
        return False

    keys = list(dict.keys())
    first_key_case = keys[0].islower()

    for key in keys[1:]:
        if key.islower() != first_key_case:
            return False

    return True

def check(candidate):
    assert candidate({ 'p': 'pineapple', 'b': 'banana' }) == True
    assert candidate({ 'p': 'pineapple', 'A': 'banana', 'B': 'banana' }) == False
    assert candidate({ 'p': 'pineapple', '5': 'banana', 'a': 'apple' }) == False
    assert candidate({ 'Name': 'John', 'Age': '36', 'City': 'Houston' }) == False
    assert candidate({ 'STATE': 'NC', 'ZIP': '12345' }) == True
    assert candidate({ 'fruit': 'Orange', 'taste': 'Sweet' }) == True
    assert candidate({  }) == False

def test_check():
    check(check_dict_case)

test_check()
