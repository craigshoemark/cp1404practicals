"""Class - Guitar."""


class Guitar:
    """Class: Guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise object data attributes."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display object string values."""
        return f"{self.name}, ({self.year}), : ${self.cost:.2f}"

    def get_age(self):
        """Calculate guitar age."""
        current_year = 2022
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Determine if guitar is vintage."""
        if self.get_age() >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        """Determine display order of guitar by age."""
        return self.year < other.year
