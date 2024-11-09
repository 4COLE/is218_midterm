"""Tests for Calculator class"""
import os
import tempfile
from app.calculator import Calculator

def test_calculator_plugin_loading():
    """Test that plugins are loaded correctly"""
    calc = Calculator()
    assert 'factorial' in calc.operations
    assert 'sqrt' in calc.operations

def test_calculate_and_log_factorial():
    """Test factorial calculation and logging"""
    calc = Calculator()
    result = calc.calculate_and_log(5, None, 'factorial')
    assert result == 120
    assert len(calc.get_history()) == 1
    assert "factorial(5) = 120" in calc.get_history()[0]

def test_calculate_and_log_invalid_operation():
    """Test invalid operation handling"""
    calc = Calculator()
    result = calc.calculate_and_log(5, 2, 'invalid_op')
    assert result == "Invalid operation."

def test_calculate_and_log_error_handling():
    """Test error handling in calculate_and_log"""
    calc = Calculator()
    result = calc.calculate_and_log(-1, None, 'factorial')
    assert "Error occurred" in result

def test_calculate_and_log_binary_operation():
    """Test binary operation calculation and logging"""
    calc = Calculator()
    result = calc.calculate_and_log(4, 2, 'add')
    assert result == 6
    assert "4 add 2 = 6" in calc.get_history()[0]

def test_load_plugins_with_invalid_plugin():
    """Test loading plugins with an invalid plugin file"""
    # Create a temporary plugin
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Create a plugins directory
        os.makedirs(os.path.join(tmpdirname, "plugins"))
        # Create an invalid plugin file
        with open(os.path.join(tmpdirname, "plugins", "invalid.py"), "w", encoding="utf-8") as f:
            f.write("# Empty plugin file")
        # Create calculator with the temporary plugins directory
        calc = Calculator()
        # This should not raise an exception and skip the invalid plugin
        assert "invalid" not in calc.operations
