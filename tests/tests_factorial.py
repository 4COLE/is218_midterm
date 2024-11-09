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

def test_factorial_large_number():
    """Test factorial with larger numbers"""
    calc = Calculator()
    result = calc.calculate_and_log(10, None, 'factorial')
    assert result == 3628800
    assert "factorial(10) = 3628800" in calc.get_history()[0]

def test_factorial_invalid_input():
    """Test factorial with invalid input types"""
    calc = Calculator()
    result = calc.calculate_and_log(1.5, None, 'factorial')
    assert "Error occurred" in str(result)

def test_factorial_history_management():
    """Test history management with factorial operations"""
    calc = Calculator()
    calc.calculate_and_log(5, None, 'factorial')
    calc.calculate_and_log(3, None, 'factorial')

    history = calc.get_history()
    assert len(history) == 2
    assert "factorial(5) = 120" in history[0]
    assert "factorial(3) = 6" in history[1]

    undone = calc.undo_last()
    assert "factorial(3) = 6" in undone
    assert len(calc.get_history()) == 1
