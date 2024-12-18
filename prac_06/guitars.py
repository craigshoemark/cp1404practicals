"""
Guitars program:
Add Guitars, print guitar details.
"""
from guitar import Guitar


def main():
    """Get guitars, display details and vintage status."""

    guitars = []

    get_guitar(guitars)

    print_report(guitars)


def get_guitar(guitars):
    """Get guitar, append to guitars, until blank name entered."""
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitars.append(Guitar(name, year, cost))

        for guitar in guitars:
            print(guitar, "added.")
        name = input("Name: ").strip()

    return guitars


def print_report(guitars):
    """Display report of all guitars."""
    print("These are my guitars:")
    name_width = max(len(guitar.name) for guitar in guitars)
    for i, guitars in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitars.is_vintage() else ""

        print(
            f"Guitar {i}: {guitars.name:>{name_width}}, ({guitars.year}), worth ${guitars.cost:10,.2f} "
            f"{vintage_string}")


main()
