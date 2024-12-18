"""Extract name from email, confirm user name, print name and email."""

# Estimated time: 1.5 hours
# Actual time: 4 hours

SPECIAL_CHARACTERS = '@'


def main():
    """Extract name from email, confirm user name, print name and email."""
    emails_and_names = {}

    email = input("Email: ").strip()
    email = get_valid_email(email)
    while email != '':
        name = get_name_from_email(email)
        is_name_correct = input(f"Is this your name {name}? (Y/n): ").strip().lower()
        if is_name_correct == 'n' or is_name_correct == 'no':
            name = input("Enter your name: ").strip().title()
        elif is_name_correct == '' or is_name_correct == 'Y':
            pass

        emails_and_names[email] = name
        email = input("Email: ").strip()

    print_report(emails_and_names)


def get_valid_email(email):
    """Prompt user for a valid email address."""
    while email != '':
        if SPECIAL_CHARACTERS in email:
            return email
        print("Email must contain '@'.")
        email = input("Email: ").strip()
    return ''


def get_name_from_email(email):
    """Get name from the email address."""
    name_part = email.split('@')[0]
    name = ' '.join(name_part.split('.')).title()
    return name


def print_report(emails_and_names):
    """Print emails and names."""
    print()
    for email, name in emails_and_names.items():
        print(f"{name} ({email})")


main()
