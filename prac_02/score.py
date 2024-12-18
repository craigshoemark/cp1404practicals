"""
CP1404 Practical
Determine score status
"""
import random


def main():
    """Get score, print the result"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    result = determine_result(score)
    random_score = random.randint(0, 100)
    random_score = determine_result(random_score)

    print(f"Your result is: {result}")
    print(f"Random score is: {random_score}")


def determine_result(score):
    """Determine the result of a score"""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
