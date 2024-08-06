"""
Class: Band
"""
from musician import Musician


class Band:
    """Band class"""

    def __init__(self, band_name=""):
        """Initialise a Band."""
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return String of Band, musicians and instrument details."""
        musicians_list = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.band_name}, {musicians_list}"

    def add(self, musician):
        """Add new musician to musicians list."""
        self.musicians.append(musician)

    def play(self):
        """Calls play() from musician.py, returns musician and instrument details."""
        return "\n".join(musician.play() for musician in self.musicians)
