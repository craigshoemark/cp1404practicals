"""Guitar: Testing"""

from guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year} ")
print()

guitar = Guitar(name, year, cost)

print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")

another_guitar = Guitar("Another Guitar", 2013, 0)

print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age()}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")
