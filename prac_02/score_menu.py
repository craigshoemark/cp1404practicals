"""Get a valid score, print score result, print 'score' length of stars"""

MENU = """(G)et score\n(P)rint result\n(S)how stars\n(Q)uit"""


def main():
    """Get valid score, print score result, print 'score' length of stars"""
    print(MENU)
    print()
    score = get_valid_score()
    choice = input("Enter your choice from menu: ").upper()

    while choice != 'Q':
        if choice == 'G':
            score = get_valid_score()
            result = determine_result(score)
            print(f"Your score is: {result}")

        elif choice == 'P':
            result = determine_result(score)
            print(f"Your score is: {result}")

        elif choice == 'S':
            print_stars(score)

        else:
            print("Invalid choice")

        print()
        print(MENU)
        print()
        choice = input("Enter your choice from menu: ").upper()

    print("Thankyou")


def get_valid_score():
    """Get a valid score with error checking"""
    score = int(input("Enter your score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter a valid score: "))
    return score


def determine_result(score):
    """Determine the result of score"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def print_stars(score):
    """Print line of stars int length of score"""
    print('*' * score)


main()
