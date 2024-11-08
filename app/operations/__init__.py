from typing import Union

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero.")
    return a / b

def modulo(a: float, b: float) -> Union[float, str]:
    if b == 0:
        return "Cannot modulo by zero."
    return a % b

def power(a: float, b: float) -> float:
    return a ** b

