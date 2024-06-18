"""Do-from-scratch Exercises"""

# "Quick Pick" Lottery Ticket Generator

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
ROW = 6


def main():
    """Generate random lottery ticket numbers."""
    number_of_picks = get_valid_quick_pick()

    for number in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_quick_picks(quick_pick)


def get_valid_quick_pick():
    """Get valid input for number of lottery numbers."""
    is_valid_input = False
    while not is_valid_input:
        try:
            number_of_picks = int(input("How many quick picks? "))
            is_valid_input = True
        except ValueError:
            print("Enter valid integer")
        else:
            return number_of_picks


def generate_quick_pick():
    """Generate random numbers, checks to ensure unique numbers in row."""
    numbers = []
    while len(numbers) < ROW:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


def print_quick_picks(quick_pick):
    """Print random lottery picks in even format."""
    quick_pick = " ".join(f"{num:2}" for num in quick_pick)
    print(quick_pick)


main()
