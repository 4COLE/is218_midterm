"""Example plugin to calculate square root of a number."""
import math
def sqrt(a):
    """Calculate square root of a number."""
    return math.sqrt(a)
plugin = {
    "sqrt": sqrt
}