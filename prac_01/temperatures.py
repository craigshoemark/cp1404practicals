"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

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
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
