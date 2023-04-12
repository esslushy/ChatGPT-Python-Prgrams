def valid_date(date: str) -> bool:
    """You have to write a function which validates a given date string and
    returns True if the date is valid otherwise False.
    The date is valid if all of the following rules are satisfied:
    1. The date string is not empty.
    2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
    3. The months should not be less than 1 or higher than 12.
    4. The date should be in the format: mm-dd-yyyy

    >>> valid_date('03-11-2000')
    True

    >>> valid_date('15-01-2012')
    False

    >>> valid_date('04-0-2040')
    False

    >>> valid_date('06-04-2020')
    True

    >>> valid_date('06/04/2020')
    False
    """
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date string into month, day, and year
    try:
        month, day, year = date.split('-')
    except ValueError:
        return False

    # Check if the month is between 1 and 12
    if not (1 <= int(month) <= 12):
        return False

    # Check the number of days based on the month and year
    if month in ['01', '03', '05', '07', '08', '10', '12']:
        max_days = 31
    elif month in ['04', '06', '09', '11']:
        max_days = 30
    elif month == '02':
        if int(year) % 4 == 0 and (int(year) % 100 != 0 or int(year) % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:
        return False

    # Check if the day is between 1 and the maximum number of days for the month
    if not (1 <= int(day) <= max_days):
        return False

    # Check if the date is in the format mm-dd-yyyy
    if len(month) != 2 or len(day) != 2 or len(year) != 4:
        return False

    return True

def check(candidate):
    assert candidate('03-11-2000') == True
    assert candidate('15-01-2012') == False
    assert candidate('04-0-2040') == False
    assert candidate('06-04-2020') == True
    assert candidate('01-01-2007') == True
    assert candidate('03-32-2011') == False
    assert candidate('') == False
    assert candidate('04-31-3000') == False
    assert candidate('06-06-2005') == True
    assert candidate('21-31-2000') == False
    assert candidate('04-12-2003') == True
    assert candidate('04122003') == False
    assert candidate('20030412') == False
    assert candidate('2003-04') == False
    assert candidate('2003-04-12') == False
    assert candidate('04-2003') == False

def test_check():
    check(valid_date)

test_check()
