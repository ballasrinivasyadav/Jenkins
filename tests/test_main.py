import sys
import os
import pytest

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import function_to_test

def test_function_to_test():
    # Arrange
    input_data = 5  # Example input
    expected_output = 10  # Expected output

    # Act
    result = function_to_test(input_data)

    # Assert
    assert result == expected_output