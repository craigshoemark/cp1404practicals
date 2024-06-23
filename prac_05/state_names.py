"""
CP1404/CP5632 Practical
State names in a dictionary
File reformatted, short state inputs can be any case,
try / except suite for (EAFP) approach.
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

for state, name in CODE_TO_NAME.items():
    print(f"{state:3} is {name}")
print()

is_valid_input = False
while not is_valid_input:
    try:
        state_code = input('Enter short state: ').upper()
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
        is_valid_input = True

    except KeyError:
        print('Enter a valid short state')
