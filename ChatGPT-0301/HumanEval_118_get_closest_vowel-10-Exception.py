def get_closest_vowel(word: str) -> str:
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    >>> get_closest_vowel('yogurt')
    'u'
    >>> get_closest_vowel('FULL')
    'U'
    >>> get_closest_vowel('quick')
    ''
    >>> get_closest_vowel('ab')
    ''
    """
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    last_consonant_index = len(word) - 1
    closest_vowel = ''
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            for j in range(i + 1, last_consonant_index):
                if word[j] in consonants:
                    closest_vowel = word[i]
                    return closest_vowel
    return closest_vowel

def check(candidate):
    assert candidate('yogurt') == 'u'
    assert candidate('full') == 'u'
    assert candidate('easy') == ''
    assert candidate('eAsy') == ''
    assert candidate('ali') == ''
    assert candidate('bad') == 'a'
    assert candidate('most') == 'o'
    assert candidate('ab') == ''
    assert candidate('ba') == ''
    assert candidate('quick') == ''
    assert candidate('anime') == 'i'
    assert candidate('Asia') == ''
    assert candidate('Above') == 'o'

def test_check():
    check(get_closest_vowel)

test_check()
