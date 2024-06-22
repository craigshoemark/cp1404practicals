"""Get a colour, print corresponding hexadecimal code."""

COLOUR_HEXADECIMAL_CODES = {'aliceblue': '#f0f8ff', 'army green': '#4b5320',
                            'banana yellow': '#ffe135', 'beige': '#f5f5dc',
                            'black coffee': '#3b2f2f', 'burgundy': '#800020',
                            'camel': '#c19a6b', 'candy apple red': '#ff0800',
                            'cardinal': '#c41e3a', 'cerulean': '#007ba7'}

colour = input("Enter colour: ").lower().strip()
while colour != "":
    try:
        if colour not in COLOUR_HEXADECIMAL_CODES:
            raise KeyError
        hexadecimal_code = COLOUR_HEXADECIMAL_CODES.get(colour)
        print(f"{colour.title()} is {hexadecimal_code}")

    except KeyError:
        print("Enter a valid colour ")
    colour = input("Enter colour: ").lower().strip()
print("Thanks")
