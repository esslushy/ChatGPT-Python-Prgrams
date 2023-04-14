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
    """
    Evaluates a basic algebraic expression specified by the given list of operators and operands.
    """

    # check that the inputs are valid
    assert len(operators) == len(operands) - 1, "Number of operators must be one less than number of operands."
    assert len(operands) >= 2, "There must be at least two operands."

    # perform the arithmetic operations in order of precedence
    result = operands[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += operands[i+1]
        elif operators[i] == "-":
            result -= operands[i+1]
        elif operators[i] == "*":
            result *= operands[i+1]
        elif operators[i] == "//":
            result //= operands[i+1]
        elif operators[i] == "**":
            result **= operands[i+1]
        else:
            raise ValueError("Invalid operator: " + operators[i])
    
    return result

def check(candidate):
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8

def test_check():
    check(do_algebra)

test_check()
