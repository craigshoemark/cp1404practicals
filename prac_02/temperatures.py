"""
CP1404/CP5632 - Practical
Temperature conversion program

display menu
get choice
while choice != Q
    if choice == C
        get Celsius
        Fahrenheit = Celsius * 9 / 5 + 32
        print Fahrenheit
    else if choice == F
        get Fahrenheit
        Celsius = 5 / 9 * (Fahrenheit - 32)
        print Celsius
    else
        print invalid message
    display menu
    get choice
print thankyou message
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert temperatures"""
    result = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            result = convert_celsius_to_fahrenheit()
        elif choice == "F":
            result = convert_fahrenheit_to_celsius()
        else:
            print("Invalid option")
        print(f"Converted temperature: {result:.2f}")
        print()
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit():
    """Convert Celsius to Fahrenheit"""
    celsius = float(input("Enter degrees Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    result = fahrenheit
    return result


def convert_fahrenheit_to_celsius():
    """Convert Fahrenheit to Celsius"""
    fahrenheit = float(input("Enter degrees Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    result = celsius
    return result


main()
