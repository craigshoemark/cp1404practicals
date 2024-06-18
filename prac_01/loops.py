# 3. Loops

# Odd numbers between 1 - 20.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C.
number_of_stars = int(input('Number of stars: '))
print(number_of_stars * '*', )

# D.
for star in range(number_of_stars + 1):
    print('*' * star)
