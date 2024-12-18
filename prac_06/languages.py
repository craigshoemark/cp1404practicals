"""
Intermediate exercises:
languages

Time Estimate for both class and client code
Estimated time: 45m
Actual: 2h
"""
from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)
print()

languages = [python, ruby, visual_basic]

print("The dynamically typed languages are: ")

for language in languages:
    if language.is_dynamic():
        print(language.name)
