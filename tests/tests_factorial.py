"""Tests for factorial function"""
import pytest
from app.calculator import Calculator

@pytest.mark.parametrize("a, operation, expected", [
    (0, 'factorial', 1),
    (1, 'factorial', 1),
    (5, 'factorial', 120),
])
def test_calculator_factorial_plugin(a, operation, expected):
    """Test dynamically loaded factorial plugin operation."""
    calc = Calculator()
    result = calc.calculate_and_log(a, None, operation)
    assert result == expected

def test_calculator_factorial_plugin_negative():
    """Test factorial plugin with negative input."""
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot calculate factorial of a negative number."):
        calc.calculate_and_log(-1, None, 'factorial')
