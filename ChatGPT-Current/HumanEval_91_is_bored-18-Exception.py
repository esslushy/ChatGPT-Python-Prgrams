def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored('Hello world')
    0
    >>> is_bored('The sky is blue. The sun is shining. I love this weather')
    1
    """
    sentences = S.split('.')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != '']
    
    sentences += S.split('?')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != '']
    
    sentences += S.split('!')
    sentences = [s.strip() for s in sentences]
    sentences = [s for s in sentences if s != '']
    
    count = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            count += 1
    
    return count

def check(candidate):
    assert candidate('Hello world') == 0
    assert candidate('Is the sky blue?') == 0
    assert candidate('I love It !') == 1
    assert candidate('bIt') == 0
    assert candidate('I feel good today. I will be productive. will kill It') == 2
    assert candidate('You and I are going for a walk') == 0

def test_check():
    check(is_bored)

test_check()
