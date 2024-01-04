import math

def addInputs(input1, input2):
    return int(input1) + int(input2)

def subtractInputs(input1, input2):
    return int(input1) - int(input2)

def multiplyInputs(input1, input2):
    return int(input1) * int(input2)

def divideInputs(input1, input2):
    try:
        return int(input1) / int(input2)
    except ZeroDivisionError:
        return "DIV0"

def modInputs(input1, input2):
    return int(input1) % int(input2)

def powerInputs(input1, input2):
    return int(input1) ** int(input2)

def squiggleInputs(input1, input2):
    input1 = int(input1) * 2
    input2 = int(input2) * 2
    return int(input1) - int(input2)

def factorialInput(input1):
    return math.factorial(int(input1))

def dollarInput(input1):
    input1 = int(input1) * 3
    return int(input1)

