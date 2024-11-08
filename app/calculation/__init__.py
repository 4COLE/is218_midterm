"""
Calculation module: abstract base class for calculator operations.
"""
import logging
from abc import ABC, abstractmethod
from typing import Union
from app.operations import addition, subtraction, multiplication, division, modulo, power

# Set up a logger for this module
logger = logging.getLogger()

class Calculation(ABC):
    """Abstract base class for calculator operations."""
    
    @abstractmethod
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Abstract method to perform a calculation."""
        pass  # pragma: no cover

class BasicCalculation(Calculation):
    """Concrete class for basic calculations with logging."""
    def calculate(self, a: float, b: float, operation: str) -> Union[float, str]:
        """Perform the operation based on the input, with logging for each operation."""
        try:
            if operation == 'add':
                result = addition(a, b)
            elif operation == 'subtract':
                result = subtraction(a, b)
            elif operation == 'multiply':
                result = multiplication(a, b)
            elif operation == 'divide':
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = division(a, b)
            elif operation == 'modulo':
                if b == 0:
                    raise ZeroDivisionError("Cannot modulo by zero.")
                result = modulo(a, b)
            elif operation == 'power':
                result = power(a, b)
            else:
                logger.warning("Invalid operation requested: %s", operation)
                return "Invalid operation."

            return result

        except ZeroDivisionError as e:
            logger.error("Division or modulo by zero error with operation %s on %s and %s", operation, a, b)
            return str(e)
        except Exception as e:
            logger.exception("An error occurred while performing the %s operation: %s", operation, e)
            return str(e)
