#!/usr/bin/env python3

import operator
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

operators = {
        #This is a dictionary!
        '+': lambda x, y : x + y,
        '-': lambda x, y : x - y,
        '*': lambda x, y : x * y,
        '/': lambda x, y : x / y,
        #'%': lambda x, y : (x+
}

def calculate(arg):
    operations = []
    for operand in arg.split():
        try:
            #This means that the operation is a number
            operand = float(operand)
            operations.append(operand)
        except ValueError:
            #Encountered a non-numeric
            function = operators[operand]
            a2 = operations.pop()
            a1 = operations.pop()
            result = function(a1, a2)
            operations.append( result )
    logger.debug(operations)
    if len(operations) != 1:
        raise TypeError


    return operations.pop()

def main():
    while True:
        print("Result: {0}".format(calculate(input("rpn calc> "))))

if __name__ == '__main__':
    main()

