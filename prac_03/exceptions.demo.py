"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():
    """Get valid numerator and denominator calculate the division, print result."""
    numerator = get_valid_numerator()
    denominator = get_valid_denominator()
    fraction = calculate_fraction(numerator, denominator)
    print(f"Result: {fraction:.2f}")


def calculate_fraction(numerator, denominator):
    """Calculate division of numerator and denominator."""
    fraction = numerator / denominator
    return fraction


def get_valid_numerator():
    """Get a valid numerator and return it."""
    is_valid_input = False
    while not is_valid_input:
        try:
            numerator = int(input("Enter the numerator: "))
            is_valid_input = True
        except ValueError:
            print("Numerator must be valid number!")
    return numerator  # no problem with potential undefined variable.


def get_valid_denominator():
    """Get a valid denominator and return it."""
    is_valid_input = False
    while not is_valid_input:
        try:
            denominator = int(input("Enter the denominator: "))
            if denominator == 0:
                print("Denominator must not be zero!")
            else:
                is_valid_input = True
        except ValueError:
            print("Denominator must be a valid number!")
    return denominator  # no problem with potential undefined variable.


main()
# 1. ValueError will handle invalid inputs: floats, alphabetic characters, symbols, or no input.

# 2. ZeroDivisionError occurs only when 0 is the denominator.

# 3. Yes, the code can be changed to avoid the possibility of ZeroDivisionError.
