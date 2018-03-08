#!/usr/bin/env python3

import operator
import logging
from math import pow
from math import sin

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

binary_operators = {
        #This is a dictionary!
        '+': lambda x, y : x + y,
        '-': lambda x, y : x - y,
        '*': lambda x, y : x * y,
        '/': lambda x, y : x / y,
        '%': lambda x, y : (x * y / 100),
        '^': lambda x, y : pow(x,y),
        '.': lambda x, y : x //y,
}

unary_operators = {
        '!': lambda x: factorial(x),
        'sin': lambda x: sin(x),
        }

def factorial(x):
    #Computes factorials of non-negative numbers recursively
    if x < 0: raise ValueError
    if x == 0: return 1
    return x * factorial(x-1)




def calculate(arg):
    operations = []
    for operand in arg.split():
        try:
            #This means that the operation is a number
            operand = float(operand)
            operations.append(operand)
        except ValueError:
            #Encountered a non-numeric

            #If it is a summation
            if operand == 'sum':
                sumOfOperations = 0
                while (operations):
                    sumOfOperations += operations.pop()
                    logging.debug(sumOfOperations)
                return sumOfOperations

            #If it is a binary operation
            try:
                function = binary_operators[operand]
                a2 = operations.pop()
                a1 = operations.pop()
                result = function(a1, a2)
                if operand == '%':
                    #The only special operation
                    operations.append(a1)
                operations.append( result )
            except KeyError:
                #If it is a unary operator
                function = unary_operators[operand]
                a1 = operations.pop()
                result = function(a1)
                operations.append( result )
    logging.debug(operations)


    return operations.pop()

def main():
    while True:
        print("Result: {0}".format(calculate(input("rpn calc> "))))

if __name__ == '__main__':
    main()

