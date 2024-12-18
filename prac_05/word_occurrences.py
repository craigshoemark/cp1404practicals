"""
Count word occurrences in a string, sort alphabetically case-insensitive.

Estimate: < 1 hour
Actual:   1.5 hours
"""

word_occurrences = {}

string = input("Enter text: ").lower()
string = list(string.split())

for word in string:
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1

max_word_length = max(len(word) for word in word_occurrences)

sorted_word_occurrences = sorted(word_occurrences.items())

for word, count in sorted_word_occurrences:
    print(f"{word:<{max_word_length}}\t: {count}")
print()
print("Thanks")
