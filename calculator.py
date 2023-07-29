import math
def add(number1, number2):
    return number1 + number2

def substract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def division(number1, number2):
    if(number2 == 0):
        return "infinity"
    else:
        return number1 / number2
    
def sqrt(number):
    return math.sqrt(number)
    
