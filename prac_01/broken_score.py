# 2. Debugging:
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= 90:
    result = "Excellent"
elif score >= 50:
    result = "Passable"
else:
    result = "Bad"
print(f"Your result is: {result}")
