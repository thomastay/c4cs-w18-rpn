#!/usr/bin/env python3

import operator

operators = {
        #This is a dictionary!
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
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
    print(operations)
    return operations.pop()

def main():
    while True:
        print("Result: {0}".format(calculate(input("rpn calc> "))))

if __name__ == '__main__':
    main()

