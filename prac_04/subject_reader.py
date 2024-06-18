"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data from file, process data, print report."""
    subject_details = load_data()

    print_report(subject_details)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    with open(FILENAME, 'r', encoding='utf-8') as input_file:  # pylint recommended including encoding
        subject_details = []
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_details.append(parts)
    return subject_details


def print_report(subject_details):
    """Print subject report."""
    for part in subject_details:
        subject = part[0]
        lecturer = part[1]
        number_of_students = part[2]
        print(f'{subject} is taught by {lecturer} and has {number_of_students} students')


main()
