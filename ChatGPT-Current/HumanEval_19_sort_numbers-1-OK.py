def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # Split the input string into a list of individual numbers
    number_list = numbers.split()
    # Convert each number to its corresponding integer value using the number_dict
    number_list = [number_dict[number] for number in number_list]
    # Sort the list of integers
    number_list.sort()
    # Convert the sorted list of integers back to a list of number strings
    number_list = [list(number_dict.keys())[list(number_dict.values()).index(number)] for number in number_list]
    # Join the list of number strings into a single string and return it
    return ' '.join(number_list)

def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

def test_check():
    check(sort_numbers)

test_check()
