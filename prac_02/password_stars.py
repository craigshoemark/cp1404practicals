"""Check length of password, print stars to match length"""
password = input("Enter a password (min 5 characters): ")
while len(password) < 5:
    print("Password must be at least 5 characters long.")
    password = input("Enter a password (min 5 characters): ")
length = len(password)
for i in range(length):
    print('*', end='')
