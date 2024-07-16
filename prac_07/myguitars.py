"""More Guitars."""

# import csv
from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read and display guitars."""
    guitars = read_guitars_from_csv(FILENAME)
    guitars.sort()
    display_guitars(guitars)


def read_guitars_from_csv(filename):
    """Read guitars from file, return list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as infile:
        for line in infile:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display list of Guitar objects."""
    for guitar in guitars:
        print(guitar)


main()
