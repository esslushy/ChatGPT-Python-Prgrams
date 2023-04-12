def fruit_distribution(s: str, n: int) -> int:
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    >>> fruit_distribution('5 apples and 6 oranges', 19)
    8
    >>> fruit_distribution('0 apples and 1 oranges', 3)
    2
    >>> fruit_distribution('2 apples and 3 oranges', 100)
    95
    >>> fruit_distribution('100 apples and 1 oranges', 120)
    19
    """
    # Split the string into a list of words
    words = s.split()

    # Initialize variables for the number of apples and oranges
    num_apples = 0
    num_oranges = 0

    # Loop through the words and count the number of apples and oranges
    for word in words:
        if word == 'apples':
            num_apples = int(words[words.index(word) - 1])
        elif word == 'oranges':
            num_oranges = int(words[words.index(word) - 1])

    # Calculate the number of mangoes
    num_mangoes = n - num_apples - num_oranges

    # Return the number of mangoes
    return num_mangoes

def check(candidate):
    assert candidate('5 apples and 6 oranges', 19) == 8
    assert candidate('5 apples and 6 oranges', 21) == 10
    assert candidate('0 apples and 1 oranges', 3) == 2
    assert candidate('1 apples and 0 oranges', 3) == 2
    assert candidate('2 apples and 3 oranges', 100) == 95
    assert candidate('2 apples and 3 oranges', 5) == 0
    assert candidate('1 apples and 100 oranges', 120) == 19

def test_check():
    check(fruit_distribution)

test_check()
