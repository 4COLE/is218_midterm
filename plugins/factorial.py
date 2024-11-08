import math

def factorial(a, *args):
    """Calculate the factorial of a number."""
    if a < 0:
        raise ValueError("Cannot calculate factorial of a negative number.")
    return math.factorial(a)

plugin = {
    "factorial": factorial
}