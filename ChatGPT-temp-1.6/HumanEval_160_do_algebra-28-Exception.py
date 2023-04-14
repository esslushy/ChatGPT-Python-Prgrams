from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    """Given two lists operator and operand, evaluate algebraic expression formed by combining
    the operands based on operator list.
    """
    # Initiate result variable to first operand of operand list
    result = operand[0]
    
    # Iterate through each operator and operand
    for i in range(1, len(operand)):
        # If operator is addition
        if operator[i-1] == '+':
            result += operand[i]
        # If operator is subtraction
        elif operator[i-1] == '-':
            result -= operand[i]
        # If operator is multiplication
        elif operator[i-1] == '*':
            result *= operand[i]
        # If operator is floor division
        elif operator[i-1] == '//':
            result //= operand[i]
        # If operator is exponentiation
        elif operator[i-1] == '**':
            result **= operand[i]
    
    # Return final result after performing all operations
    return result

def check(candidate):
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8

def test_check():
    check(do_algebra)

test_check()
