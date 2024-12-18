"""
Class: UnreliableCar
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Class for UnreliableCar,
    random reliability score determines if object will drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar instance based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.reliability = reliability

    def __str__(self):
        """Return string based on parent class Car."""
        return f"{super().__str__()}"

    def get_score(self):
        """Get random number for reliability. """
        return random.randint(0, 100)

    def drive(self, distance):
        """Drive like parent Car when get_score() < reliability."""

        if self.get_score() < self.reliability:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven
        else:
            distance = 0
