def encode(message: str) -> str:
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    vowels = 'aeiouAEIOU'
    encoded = ''
    for letter in message:
        if letter.isalpha():
            if letter in vowels:
                encoded += chr(ord(letter) + 2)
            else:
                encoded += letter.swapcase()
        else:
            encoded += letter
    return encoded

def check(candidate):
    assert candidate('TEST') == 'tgst'
    assert candidate('Mudasir') == 'mWDCSKR'
    assert candidate('YES') == 'ygs'
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG'
    assert candidate('I DoNt KnOw WhAt tO WrItE') == 'k dQnT kNqW wHcT Tq wRkTg'

def test_check():
    check(encode)

test_check()
