def main():
    """Check length of password, print stars to match password length"""
    password = get_password()
    print_password(password)


def print_password(password):
    for i in range(len(password)):
        print('*', end='')


def get_password():
    password = input("Enter a password (min 5 characters): ")
    while len(password) < 5:
        print("Password minimum 5 characters required.")
        password = input("Enter a password (minimum 5 characters): ")
    return password


main()
