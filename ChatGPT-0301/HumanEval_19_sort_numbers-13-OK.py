def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_dict = {
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
    num_list = numbers.split()
    # Convert each number to its corresponding integer value using the dictionary
    num_list = [num_dict[num] for num in num_list]
    # Sort the list of integers
    num_list.sort()
    # Convert the sorted list of integers back to their corresponding string values
    sorted_numbers = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    # Join the sorted list of string values into a single string and return it
    return ' '.join(sorted_numbers)

def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

def test_check():
    check(sort_numbers)

test_check()
