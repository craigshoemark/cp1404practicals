"""Password check program"""


def main():
    """Check length of password, print stars to match password length"""
    password = get_password()
    print_password(password)


def print_password(password):
    """Print stars to match length of password"""
    print('*' * len(password))


def get_password():
    """Get password of valid length"""
    password = input("Enter a password (min 5 characters): ")
    while len(password) < 5:
        print("Password minimum 5 characters required.")
        password = input("Enter a password (minimum 5 characters): ")
    return password


main()
