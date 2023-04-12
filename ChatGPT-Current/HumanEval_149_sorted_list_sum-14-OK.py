from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    >>> list_sort(['aa', 'a', 'aaa'])
    ['aa']
    >>> list_sort(['ab', 'a', 'aaa', 'cd'])
    ['ab', 'cd']
    """
    # Filter out strings with odd lengths
    filtered_lst = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    sorted_lst = sorted(filtered_lst, key=lambda s: (len(s), s))
    
    return sorted_lst

def check(candidate):
    assert candidate(['aa', 'a', 'aaa']) == ['aa']
    assert candidate(['school', 'AI', 'asdf', 'b']) == ['AI', 'asdf', 'school']
    assert candidate(['d', 'b', 'c', 'a']) == []
    assert candidate(['d', 'dcba', 'abcd', 'a']) == ['abcd', 'dcba']
    assert candidate(['AI', 'ai', 'au']) == ['AI', 'ai', 'au']
    assert candidate(['a', 'b', 'b', 'c', 'c', 'a']) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ['cc', 'dd', 'aaaa', 'bbbb']

def test_check():
    check(sorted_list_sum)

test_check()
