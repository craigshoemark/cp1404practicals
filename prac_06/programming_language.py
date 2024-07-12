"""
Intermediate exercises:
Class Programming Language

Time Estimate for both class and client code
Estimated time: 45m
Actual: 2h
"""


class ProgrammingLanguage:
    """Class: Programming Language."""

    def __init__(self, name="", typing="", reflection="", year=""):
        """Initialise object data attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Print object string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Check if language is dynamically typed."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
