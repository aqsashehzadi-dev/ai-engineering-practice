"""Utility functions for basic calculations."""
DEFAULT_TAX_RATE = 0.10
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def calculate_tax(amount):
    return amount * DEFAULT_TAX_RATE
if __name__ == "__main__":
    print("Calculator module name:", __name__)