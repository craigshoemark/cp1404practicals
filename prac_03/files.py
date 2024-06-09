"""Do-from-scratch Exercises"""
# Files

# 1.
"""Get user name, write name to file."""
outfile = open('name.txt', 'w')
name = input("Please enter name: ")
print(name, file=outfile)
outfile.close()

# 2.
"""Read name from file, print greeting."""
infile = open('name.txt', 'r')
name = infile.read().strip()
infile.close()
print(f"Hi {name}!")

# 3.
"""Print total of first 2 lines."""
infile = open('numbers.txt', 'r')
number_1 = int(infile.readline())
number_2 = int(infile.readline())
infile.close()
total = number_1 + number_2
print(total)

# 4.
"""Print total of all lines."""
with open('numbers.txt', 'r') as infile:
    total = 0
    for line in infile:
        line = int(line)
        total += line
    print(total)
