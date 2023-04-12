from typing import List

def match_parens(lst: List[str]) -> str:
    """
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    >>> match_parens(['()(', ')'])
    'Yes'
    >>> match_parens([')', ')'])
    'No'
    """
    # Concatenate the two strings in the list
    s = lst[0] + lst[1]
    stack = []
    # Iterate over each character in the concatenated string
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            # If the stack is empty, it means there is no matching opening bracket
            if not stack:
                return 'No'
            # Pop the last opening bracket from the stack
            stack.pop()
    # If the stack is empty, it means all brackets are matched
    if not stack:
        return 'Yes'
    else:
        return 'No'

def check(candidate):
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes'

def test_check():
    check(match_parens)

test_check()
