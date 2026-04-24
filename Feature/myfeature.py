#!/usr/bin/env python3
"""
Basic Python Feature Module

This module provides a basic calculator feature.
"""

class BasicCalculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    """Demo the calculator feature."""
    calc = BasicCalculator()
    print("Basic Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

if __name__ == "__main__":
    main()

print('welcome to devasc')