"""More Guitars."""

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read, display and add guitars to file."""
    guitars = read_guitars_from_csv(FILENAME)
    guitars.sort()
    display_guitars(guitars)

    print("Add new guitar")
    add_guitar(guitars)

    save_guitars_to_file(FILENAME, guitars)


def read_guitars_from_csv(filename):
    """Read guitars from file, return list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as infile:
        for line in infile:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def add_guitar(guitars):
    """Get guitars, append to guitars, until a blank name is entered."""
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display list of Guitar objects."""
    for guitar in guitars:
        print(guitar)


def save_guitars_to_file(filename, guitars):
    """Save guitars to csv file, overwriting current data."""
    with open(filename, 'w') as outfile:
        for guitar in guitars:
            line = f"{guitar.name},{guitar.year},{guitar.cost}"
            outfile.write(line + '\n')


main()
