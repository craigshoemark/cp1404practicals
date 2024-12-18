"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
REQUIRED_INPUT = 1
COUNT = 1


def main():
    """Program to get and check a user's password."""
    print_instructions()
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def print_instructions():
    """Print program instructions."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) <= MIN_LENGTH or len(password) >= MAX_LENGTH:
        return False

    number_of_lower = 0
    number_of_upper = 0
    number_of_digit = 0
    number_of_special = 0

    for character in password:
        if character.islower():
            number_of_lower += COUNT
            # COUNT may not be needed here, only to update globally,
            # cant think a situation where it would change or be other than 1?
        if character.isupper():
            number_of_upper += COUNT

        if character.isdigit():
            number_of_digit += COUNT

        if character in SPECIAL_CHARACTERS:
            number_of_special += COUNT

    if (number_of_digit >= REQUIRED_INPUT and
            number_of_lower >= REQUIRED_INPUT and
            number_of_upper >= REQUIRED_INPUT):
        if IS_SPECIAL_CHARACTER_REQUIRED:
            if number_of_special < REQUIRED_INPUT:
                return False
            return True
        return True
    return False


main()
