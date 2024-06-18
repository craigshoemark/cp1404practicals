"""Lists warm-up"""
numbers = [3, 1, 4, 1, 5, 9, 2]

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers.insert(0, "ten")
print(numbers)

# 2. Change the last element of numbers to 1
numbers.insert(8, 1)
print(numbers)

# 3. Print all the elements from numbers except the first two (slice)
numbers = numbers[3:]
print(numbers)

# 4. Print whether 9 is an element of numbers
if 9 in numbers:
    print("True")
else:
    print("False")
